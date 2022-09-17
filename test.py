#!/bin/python3

import math
import os
import random
import re
import sys
import threading
import time
import copy

        

class InventoryStore:
    ### In memory Data stores ###
    ## Inventory Data store
    ## {
    ##    "product_id": {"name": "", "count": XX}
    ## }
    inventory = {}

    def __init__(self):
        super().__init__()
        self._inventory_lock = threading.Lock()
        
    def removeFromInventory(self, productId, count):
            success = False
        #with self._inventory_lock:
            self.inventory[productId]["count"] -= count
            # inventory goes to -ve cancel the order.
            if self.inventory[productId]["count"] < 0:
                self.inventory[productId]["count"] += count
            else:
                success = True
            return success
    
    def addToInventory(self, productId, count):
        with self._inventory_lock:
            self.inventory[productId]["count"] += count
    
    def isProductInInventory(self, productId, count):
        return productId in self.inventory and self.inventory[productId]["count"] >= count

    def getProductCount(self, productid):
        return self.inventory.get(productid, 0)
        
    def createProduct(self, productId, name, count):
        if self.isProductInInventory(productId, 0):
            raise Exception("Product already exists in the Inventory - " + productId)
        
        # check if thread safe needed here
        self.inventory[productId] = {"name": name, "count": count}


class Inventory:
    
    MAX_BLOCK_TIME = 300 # secs

    ## Inventory block data store
    ## {
    ##    "orderid": {"product_id": "", "count": XX, "time": <second from epoch>}
    ## }
    ##
    blocked_inventory = {}
    
    def __init__(self):
        super().__init__()
        self.inventory_store = InventoryStore()
    
    def createProduct(self, productId, name, count):
        self.inventory_store.createProduct(productId, name, count)

    def getinventory(self, productId):
        if self.inventory_store.isProductInInventory(productId, 0):
            return self.inventory_store.getProductCount(productId)
        else:
            raise Exception("No product found with id - " + productId)
        
    def blockInventory(self, productId, count, orderId):
        if orderId in self.blocked_inventory:
            raise Exception("Duplicate req - Order already present in inventory")
    
        #if not self.inventory_store.isProductInInventory(productId, count):
        #    raise Exception("required count for product not in inventory")
        
        if self.inventory_store.removeFromInventory(productId, count):
                self.blocked_inventory[orderId] = {
		    "productId": productId, "count": count,
		    "time": time.time()
                }
        else:
                print("could not block inventory")
        
    def confirmOrder(self, orderId):
        if not self._isOrderInBlockedInventory(orderId):
            raise Exception("Order not found")
            
        del self.blocked_inventory[orderId] # check if this information needs to sent somewhere
    
    def releaseBlockedInventory(self, orderId):
        if not self._isOrderInBlockedInventory(orderId):
            raise Exception("Order not found")
        
        order_details = self.blocked_inventory[orderId]
        productId = order_details["productId"]
        count = order_details["count"]
        
        # do we need to check again if product is still in inventory?
        self.inventory_store.addToInventory(productId, count)
        
        del self.blocked_inventory[orderId]
        
    def _isOrderInBlockedInventory(self, orderId):
        return orderId in self.blocked_inventory
    
    def getAllBlockedInventory(self):
        return self.blocked_inventory
    

def analyseBlockedInventoryForRelease(inventory):
    # for every order thats in blocked state for more than 5 mins, move back to inventory
    blocked_inventory = inventory.getAllBlockedInventory()
    while(True):
        time.sleep(.1) # 1 secs
        print(blocked_inventory)
        if not blocked_inventory:
            continue
        print("evicting")
        evict_threshold = time.time() - 200
        for key, value in copy.copy(blocked_inventory).items():
            if value["time"] <= evict_threshold:
                inventory.releaseBlockedInventory(key)

def test1(inventory):
    inventory.blockInventory("1", 5, "1")
    inventory.blockInventory("1", 4, "2")

def test2(inventory):
    inventory.blockInventory("1", 1, "3")
    inventory.blockInventory("1", 1, "5")

def testa(inventory):
    inventory.createProduct("1", "ABC", 10)
    #inventory.createProduct("2", "XYZ", 1)
    #inventory.createProduct("3", "LMN", 0)
    
    print(inventory.getinventory("1"))
    #print(inventory.getinventory("2"))
    #print(inventory.getinventory("3"))
    
    inventory.blockInventory("1", 6, "1") # pass
    
    inventory.blockInventory("1", 6, "2") # fail
    
    time.sleep(3)
    
    inventory.blockInventory("1", 6, "3") # pass
    
    inventory.confirmOrder("3")
    
    inventory.blockInventory("1", 6, "4") # fail
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ## productid = input()

    ## result = getinventory(productid)
    
    inventory = Inventory()
    
    #blockInventoryClearThread = threading.Thread(target=analyseBlockedInventoryForRelease, args=(inventory, ))
    #blockInventoryClearThread.start()
    
    inventory.createProduct("1", "ABC", 10)

    #thread1 = threading.Thread(target=testa, args=(inventory, ))
    #thread1.start()

    ## blockInventoryClearThread.join()
    
    ## Testing
    thread1 = threading.Thread(target=test1, args=(inventory, ))
    thread2 = threading.Thread(target=test2, args=(inventory, ))
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    # fptr.write(str(result) + '\n')

    # fptr.close()
