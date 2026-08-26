TICKETS=[
    {"id":1,"category":'账号','priority':2},
    {'id':2,'category':'支付','priority':1},
    {'id':3,'category':'账号','priority':3},
]

def count_by_category(tickets:list[dict])->dict:
    counts={}
    for ticket in tickets:
        category=ticket['category']
        counts[category]=counts.get(category,0)+1
    return counts


def get_unique_categories(tickets:list[dict])->dict:
    unique_categories=set()
    for ticket in tickets:
        unique_categories.add(ticket['category'])
    return unique_categories


def sort_by_priority(tickets:list[dict])->list[dict]:
    return sorted(tickets,key=lambda ticket:ticket['priority'])


def print_category_counts(counts: dict) -> None:
    print("各类别工单数量：")
    for category in sorted(counts):
        print(f"{category}: {counts[category]}")



def print_unique_categories(unique_categories: set) -> None:
    print("不重复类别：")
    for category in sorted(unique_categories):
        print(f"{category}")


def print_sorted_tickets(tickets: list[dict]) -> None:
    print("按优先级排序：")
    for ticket in tickets:
        print(
            f"工单 {ticket['id']}: "
            f"类别={ticket['category']}, 优先级={ticket['priority']}"
        )


def main():
    category_counts=count_by_category(TICKETS)
    unique_categories=get_unique_categories(TICKETS)
    sorted_tickets=sort_by_priority(TICKETS)

    print_category_counts(category_counts)
    print()
    print_unique_categories(unique_categories)
    print()
    print_sorted_tickets(sorted_tickets)

if __name__ == "__main__":
    main()