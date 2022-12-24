class TreeStore:
    def __init__(self, items: list[dict]) -> None:
        self.items = items

    def getAll(self):
        return self.items
    
    def getItem(self, id: int):
        return filter(lambda dict_item: dict_item["id"] == id, self.items).__next__()
    
    def getChildren(self, id) -> list[dict]:
        return list(filter(lambda dict_item: dict_item["parent"] == id, self.items))
    
    def getAllParents(self, id: int) -> list[dict]:
        list_of_parrent = []
        parrent_id = None

        for dict_items in self.items:
            if dict_items['id'] == id:
                if not dict_items['parent'] == "root":
                    parrent_id = dict_items['parent']
                else:
                    return list_of_parrent
        
        for dict_items in self.items:
            if dict_items['id'] == parrent_id:
                list_of_parrent.append(dict_items)
                return list_of_parrent + self.getAllParents(parrent_id)
