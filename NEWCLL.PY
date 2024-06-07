#PROGRme for code for circular linked list

#programme to create a node
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

#programme for circular linked list 

class cll:
    def __init__(self,last=None):
        self.last=last
    
    #method to check the empty of the list
    
    def isempty(self):
        if self.last==None:
            return None
        else:
            return self.last
        
    #sir method
    # def is_empty(self):
    #     return self.last==None
        
    #method to add at start
    
    def addatstart(self,data):
        k=Node(data) #creating a node
        if self.isempty()==None:
            k.next=k
            self.last=k
        else:
            k.next=self.last.next  #copying first node to new node
            self.last.next=k     #copying new node to last node
            
            
    #method to add at last
    
    def addatlast(self,data):
        k=Node(data)
        if self.isempty()==None:  #is list is empty
            k.next=k
            self.last=k
        elif self.last.next==None:  # if one element is present 
            k.next=self.last.next
            self.next=k
        else:                #if more than one element is present
            k.next=self.last.next
            self.last.next=k
            self.last=k
      #code to search the element       
    def search(self,data):   
        temp=self.start.next  # in this we are assingin alternate node to temp
        if self.isempty()==None:
            return None
        else: # 
            while temp!=self.last:
                if temp.item==data:
                    return temp
                else:
                    temp=temp.next
            if temp.item==data:
                return temp
            else:
                return None
    
    # method to add after specific element
    
    def addatspecific(self,temp,data):
        if temp is not None: # if list has element 
            n=Node(data,temp.next)
            temp.next=n   
            if temp==self.last:
                self.last=n
                
    # method to delete first
    def delatstart(self):
        if self.isempty()==None:
            pass
        elif self.last.next.next==self.last:
            self.last.next=None
        elif self.last.next==None:
            self.last=None
        else:
            self.last.next=self.last.next.next
            
    # method to delete last
     
    def delatlast(self):
        temp=self.last.next
        while temp!=self.last:
            temp=temp.next
        if self.isempty()==None:
            pass
        elif self.last.next==None:
            self.last=None
        else:
            temp.next=temp.next.next
            self.last=temp
        
        
    #method to print list

    
    def printlist(self):
        temp=self.last.next
        if self.isempty()==None:
            print("List is empty")
        elif self.last.next==None:
            print("List is empty")
        else:
            while temp!=self.last:
                print(temp.item)
                temp=temp.next
            print(temp.item)
            
            
#driver code
mylist=cll()
mylist.addatstart(23)
mylist.addatstart(89)
mylist.addatstart(67)
mylist.addatstart(56)
mylist.addatlast(12)
mylist.addatlast(99)
mylist.delatstart()
mylist.delatlast()
# mylist.delatlast()
# mylist.delatlast()
# mylist.delatlast()
# mylist.delatlast()
# mylist.delatstart()
mylist.printlist()  