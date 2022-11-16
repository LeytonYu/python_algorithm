from pprint import pprint

import openpyxl
from openpyxl.styles import Alignment

header_test = [
    {
        "name": "月份",
        "map": "month"
    },
    {
        "name": "总计",
        "children": [
            {
                "name": "金额（元）",
                "map": "total_money",
                # 'children': [
                #     {
                #         "name": "nmd",
                #         "map": "wsm",
                #     }
                # ]
            },
            {
                "name": "上年同期金额（元）",
                "map": "last_total_money"
            },
            {
                "name": "同比增长率",
                "map": "total_percent"
            }
        ]
    },
    {
        "name": "数据营销部",
        "children": [
            {
                "name": "金额（元）",
                "map": "data_money",
                "taichi": 2
            },
            {
                "name": "上年同期金额（元）",
                "map": "last_data_money",
                "taichi": 2
            },
            {
                "name": "同比增长率",
                "map": "data_percent"
            }
        ]
    },
    {
        "name": "人才营销部",
        "children": [
            {
                "name": "金额（元）",
                "map": "talent_money",
                "taichi": 1
            },
            {
                "name": "上年同期金额（元）",
                "map": "last_talent_money",
                "taichi": 1
            },
            {
                "name": "同比增长率",
                "map": "talent_percent"
            }
        ]
    }
]


class ExportExcelUltra:

    def _get_data_depth(self, header):
        depth = 1
        q = [(i.get('children'), depth + 1) for i in header if i.get('children')]
        max_depth = 1
        while q:
            n, depth = q.pop()
            max_depth = max(max_depth, depth)
            q = q + [(i.get('children'), depth + 1) for i in n if i.get('children')]

        return max_depth

    def _get_data_weight(self, header):
        weight = 0
        for obj in header:
            tbj = obj
            if tbj.get('children'):
                lst = tbj.get('children')
                mw = self._get_data_weight(lst)
                weight += mw
            else:
                weight += 1
        return weight

    def _deal_header(self, raw_header, merge_cell):
        head = {}
        header_key = []
        depth = self._get_data_depth(raw_header)
        if depth <= 1:
            for obj in raw_header:
                head[obj['map']] = obj['name']
            header = [list(head.values())]
            header_key = list(head.keys())
        else:
            header = [[] for i in range(depth)]
            queue = raw_header
            for i in range(depth):
                tp = []
                col = 1
                for obj in queue:
                    if i == depth - 1:
                        header_key.append(obj['map'])
                    if obj.get('pass'):
                        tp.append(obj)
                        col += 1
                        continue
                    child = obj.pop('children', None)
                    if not child:
                        for h in header[i:depth]:
                            h.insert(col - 1, obj['name'])
                        if i + 1 != depth:
                            merge_cell.append([i + 1, col, depth, col])
                        col += 1
                        head[obj['map']] = obj['name']
                        obj['pass'] = True
                        tp.append(obj)
                    else:
                        o_weight = self._get_data_weight(child)
                        o_depth = i + 1 if self._get_data_depth(child) else depth
                        for h in header[i: o_depth]:
                            for ow in range(o_weight):
                                h.insert(col - 1 + ow, obj['name'])
                        merge_cell.append([i + 1, col, depth - o_depth, col + o_weight - 1])
                        col += o_weight
                        tp.extend(child)
                queue = tp
        return header_key, header

    def _deal_body(self, raw_body, merge_cell, header_key, row):
        depth = self._get_data_depth(raw_body)
        if depth <= 1:
            return raw_body
        else:
            weight = self._get_data_weight(raw_body)
            body = [{} for i in range(weight)]
            tp = []
            for i in range(depth):
                start = 0
                for obj in raw_body:
                    key = header_key[i]
                    value = obj[key]
                    children = obj.get('children')
                    if children:
                        o_weight = self._get_data_weight(children)
                        for dct in body[start: start + o_weight]:
                            dct[key] = value
                        if o_weight > 1:
                            merge_cell.append((start + row, i+1, start + row + o_weight - 1, i + 1))
                        start += o_weight
                        tp.extend(children)
                    else:
                        body[start].update(obj)
                        start += 1
                raw_body = tp
                tp = []
            return body

    def form_export_template(self, data):
        raw_header = data.get('header')
        raw_body = data.get('body')
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        merge_cell = []
        header_key, header = self._deal_header(raw_header=raw_header, merge_cell=merge_cell)
        body = self._deal_body(raw_body, merge_cell, header_key, len(header)+1)
        for h in header:
            sheet.append(h)
        for obj in body:
            sheet.append([obj.get(v) for v in header_key])
        self.format_excel(merge_cell, sheet)
        workbook.save('excel_render_test.xlsx')
        return workbook

    def format_excel(self, merge_cell, sheet):
        for sr, sc, er, ec in merge_cell:
            sheet.merge_cells(start_row=sr, start_column=sc, end_row=er, end_column=ec)
        alignment = Alignment(horizontal='center', vertical='center', wrapText=True)
        for rows in sheet:
            for row in rows:
                row.alignment = alignment


def run_excel_export():
    excel_object = ExportExcelUltra()
    data = {
        "header": [
            {
                "name": "产品大类",
                "map": "bp"
            },
            {
                "name": "产品小类",
                "map": "sp"
            },
            {
                "name": "1月",
                "map": "1"
            },
            {
                "name": "2月",
                "map": "2"
            },
            {
                "name": "3月",
                "map": "3"
            },
            {
                "name": "Q1总计",
                "map": "Q1"
            }
        ],
        "body": [
            {
                "bp": "人才服务",
                "children": [
                    {
                        "1": "385760.00",
                        "2": "202800.00",
                        "3": "2252000.00",
                        "sp": "人才在线服务",
                        "pid": 25,
                        "Q1": "2840560.00"
                    },
                    {
                        "1": 0,
                        "2": 0,
                        "3": "52500.00",
                        "sp": "人才邀约服务",
                        "pid": 50,
                        "Q1": "52500.00"
                    },
                    {
                        "1": 0,
                        "2": 0,
                        "3": "65600.00",
                        "sp": "星云人才引进数字系统",
                        "pid": 49,
                        "Q1": "65600.00"
                    }
                ]
            },
            {
                "bp": "媒体服务",
                "children": [
                    {
                        "1": "20000.00",
                        "2": "12000.00",
                        "3": "48000.00",
                        "sp": "媒体在线服务",
                        "pid": 24,
                        "Q1": "80000.00"
                    }
                ]
            },
            {
                "bp": "学术服务",
                "children": [
                    {
                        "1": "6000.00",
                        "2": 0,
                        "3": 0,
                        "sp": "学术在线服务",
                        "pid": 56,
                        "Q1": "6000.00"
                    }
                ]
            }
        ]
    }
    excel_object.form_export_template(data)


if __name__ == '__main__':
    run_excel_export()
