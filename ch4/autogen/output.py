import streamlit as st
import requests

DEFAULT_USD_CNY = 7.25
DEMO_BTC_PRICE = 63154.13
DEMO_BTC_CHANGE = 2.56

# 数据获取函数
def get_bitcoin_price():
    huobi_url = 'https://api.huobi.pro/market/detail/merged?symbol=btcusdt'
    coingecko_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true'
    errors = []

    try:
        response = requests.get(huobi_url, timeout=(3, 6))
        response.raise_for_status()
        data = response.json()
        tick = data['tick']

        current_price = float(tick['close'])
        open_price = float(tick['open'])
        price_change_percentage = ((current_price - open_price) / open_price) * 100
        return current_price, price_change_percentage, None
    except requests.exceptions.RequestException as e:
        errors.append(f"Huobi: {e}")
    except (KeyError, ValueError, ZeroDivisionError) as e:
        errors.append(f"Huobi 返回格式异常: {e}")

    try:
        response = requests.get(coingecko_url, timeout=(3, 6))
        response.raise_for_status()
        data = response.json()

        current_price = data['bitcoin']['usd']
        price_change_percentage = data['bitcoin']['usd_24h_change']
        return current_price, price_change_percentage, None
    except requests.exceptions.RequestException as e:
        errors.append(f"CoinGecko: {e}")
    except (KeyError, ValueError) as e:
        errors.append(f"CoinGecko 返回格式异常: {e}")

    return None, None, "连接价格接口失败: " + " | ".join(errors)

def get_usd_cny_rate():
    rate_url = 'https://open.er-api.com/v6/latest/USD'

    try:
        response = requests.get(rate_url, timeout=(3, 5))
        response.raise_for_status()
        data = response.json()
        if data.get('result') != 'success':
            raise ValueError(data.get('error-type', '汇率接口返回失败状态'))
        rate = float(data['rates']['CNY'])
        return rate, None
    except requests.exceptions.RequestException as e:
        return DEFAULT_USD_CNY, f"汇率接口连接失败，已使用默认汇率 {DEFAULT_USD_CNY}: {e}"
    except (KeyError, ValueError) as e:
        return DEFAULT_USD_CNY, f"汇率接口返回格式异常，已使用默认汇率 {DEFAULT_USD_CNY}: {e}"

# 初始化 Streamlit 应用
st.title('实时比特币价格')
st.subheader('获取最新的比特币价格信息及其24小时价格变化趋势')

if "btc_price" not in st.session_state:
    st.session_state.btc_price = None
    st.session_state.btc_change = None
    st.session_state.is_demo_data = False
    st.session_state.usd_cny_rate = DEFAULT_USD_CNY
    st.session_state.btc_error = None
    st.session_state.rate_warning = None

# 添加刷新按钮
if st.button('获取/刷新价格'):
    # 显示加载状态
    with st.spinner('正在获取价格，最多等待 5 秒...'):
        current_price, price_change_percentage, error = get_bitcoin_price()
        usd_cny_rate, rate_warning = get_usd_cny_rate()
        if error:
            current_price = DEMO_BTC_PRICE
            price_change_percentage = DEMO_BTC_CHANGE

        st.session_state.btc_price = current_price
        st.session_state.btc_change = price_change_percentage
        st.session_state.is_demo_data = bool(error)
        st.session_state.usd_cny_rate = usd_cny_rate
        st.session_state.btc_error = error
        st.session_state.rate_warning = rate_warning

# 显示数据
if st.session_state.btc_price is not None:
    btc_rmb_price = st.session_state.btc_price * st.session_state.usd_cny_rate

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="当前比特币价格 (USD)", value=f"${st.session_state.btc_price:,.2f}")
    with col2:
        st.metric(label="当前比特币价格 (RMB)", value=f"¥{btc_rmb_price:,.2f}")

    if st.session_state.btc_change is not None:
        st.metric(label="24小时变化 (%)", value=f"{st.session_state.btc_change:.2f}%")

    st.caption(f"换算汇率: 1 USD = {st.session_state.usd_cny_rate:.4f} CNY")
    if st.session_state.is_demo_data:
        st.warning(f"真实行情接口暂时不可用，当前显示演示数据。错误信息: {st.session_state.btc_error}")
    if st.session_state.rate_warning:
        st.warning(st.session_state.rate_warning)
elif st.session_state.btc_error:
    st.error(st.session_state.btc_error)
else:
    st.info("点击“获取/刷新价格”开始获取比特币价格。")
