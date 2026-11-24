"""仪表盘视图：只做展示，数据由调用方提供。"""
import sqlite3


def render_dashboard(db_path):
    conn = sqlite3.connect(db_path)
    total = conn.execute("select sum(amount) from invoices").fetchone()[0]
    return f"总计：{total}"


def tax(amount):
    return amount * 0.0825


def format_kind(kind):
    if kind == "shop":
        return "订单"
    elif kind == "service":
        return "服务"
    return "其他"
