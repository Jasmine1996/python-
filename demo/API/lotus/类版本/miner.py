class miner:
    def __init__(self, miner_id, location, target_power):
        self.miner_id = miner_id
        self.location = location
        self.target_power = target_power


    def get_discripetion_info(self):
        long_name = f"{self.location}\t{self.miner_id}\t{self.target_power}\n"
        return long_name

f054412 = miner("嘉兴", 'f054412', '1.5P')
f054412.get_discripetion_info()

