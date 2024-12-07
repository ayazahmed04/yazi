class ItemPipeline:
    def process_item(self, item):
        """Process save the item(you can extend this with with saving to csv)"""
        print(f"Processing item : {item}")
        # save item e.g., to csv 
        return item
        