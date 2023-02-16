from IPG import IPG, IPG_status
from typing import List

class BurnInBoard():
    
    IPG_in_board = 2
    
    def __init__(self,id):
        self.idNum = id
        self.IPGs = [IPG(id) for id in range(BurnInBoard.IPG_in_board)]
        self.burnin_active = False
        
    def updateStatus(self, statuses : List[IPG_status]):
        for ipg_idx in range(BurnInBoard.IPG_in_board):
            self.IPGs[ipg_idx].status = statuses[ipg_idx]

    def setBurnIn(self, active : bool):
        self.burnin_active = active

    def isBurnInActive(self):
        return self.burnin_active
    