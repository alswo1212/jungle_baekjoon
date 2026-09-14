from collections import defaultdict

def solution(id_list:list[str], report:list[str], k:int):
    mail_receive = defaultdict(set)
    report_map = defaultdict(set)

    for ft in report:
        reporter, to = ft.split()
        report_map[to].add(reporter)
        
    for key in report_map.keys():
        if len(report_map[key]) >= k:
            for id in report_map[key]:
                mail_receive[id].add(key)

    return list(map(lambda id: len(mail_receive[id]) ,id_list))