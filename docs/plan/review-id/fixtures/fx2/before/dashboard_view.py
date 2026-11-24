"""仪表盘视图：只做展示，数据由调用方提供。"""


def render_dashboard(summary):
    return f"总计：{summary['total']}"


def format_kind(kind):
    return kind
