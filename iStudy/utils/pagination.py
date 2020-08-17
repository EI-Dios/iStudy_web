class Pagination:

    def __init__(self, request, data_length, per_num=10, max_show=11):
        try:
            page = int(request.GET.get('page', 1))
            if page <= 0:
                page = 1
        except Exception:
            page = 1
        # 每页显示的数据条数
        # per_num = 10

        qd = request.GET.copy()

        # 总的页码数
        total_num, more = divmod(data_length, per_num)
        if more:
            total_num += 1
        # 显示的页码数
        # max_show = 11
        half_show = max_show // 2
        if total_num <= max_show:
            # 页码的起始值
            page_start = 1
            # 页码的终止值
            page_end = total_num
        else:
            page_start = page - half_show
            page_end = page + half_show
            if page_start <= 0:
                page_start = 1
                page_end = max_show
            elif page_end >= total_num:
                page_start = total_num - max_show + 1
                page_end = total_num
        page_list = ['<nav aria-label="Page navigation"><ul class="pagination pull-right">']

        if page == 1:
            page_list.append('<li class="disabled"><a><span aria-hidden="true">&laquo;</span></a></li>')
        else:
            qd['page'] = page - 1
            page_list.append(
                '<li><a href="?{}"><span aria-hidden="true">&laquo;</span></a></li>'.format(qd.urlencode()))
        for i in range(page_start, page_end + 1):
            qd['page'] = i
            if i == page:
                page_list.append('<li class="active"><a href="?{}">{}</a></li>'.format(qd.urlencode(), i))
            else:
                page_list.append('<li><a href="?{}">{}</a></li>'.format(qd.urlencode(), i))

        if page == total_num:
            page_list.append('<li class="disabled"><a><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            qd['page'] = page + 1
            page_list.append(
                '<li><a href="?{}"><span aria-hidden="true">&raquo;</span></a></li>'.format(qd.urlencode()))

        page_list.append('</ul></nav>')

        self.page_html = ''.join(page_list)
        # 切片的起始值
        self.start = (page - 1) * per_num
        # 切片的终止值
        self.end = page * per_num