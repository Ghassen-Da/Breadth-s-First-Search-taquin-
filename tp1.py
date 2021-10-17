import random

class State:
    size = 2
    initial_state = []
    final_state= []
    next_states = []
    visited_states=[]


    def taquin_bfs(self):
        self.setSize()
        self.final_state=self.setFinalState()
        self.initial_state=self.sefInitialState()
        self.visited_states.append(self.initial_state)
        self.next_states.append(self.initial_state)
        print(self.initial_state)
        self.setNextStates(self.initial_state)
        while(self.next_states):
            state=self.next_states.pop(0)
            print (state, end = "\n")
            if state == self.final_state:
                print('found')
                return
            elif state not in self.visited_states:
                self.visited_states.append(state)
                self.setNextStates(state)
            # print(len(self.visited_states))
        print('not found')
        return 
            
            



    def setSize(self):
        self.size = int(input("Write the size of the square: "))
    
    def sefInitialState(self):
        self.initial_state.append(' ')
        for x in range(self.size**2-1):
            self.initial_state.append(x+1)
        random.shuffle(self.initial_state)
        return self.initial_state

    def setFinalState(self):
        self.final_state.append(' ')
        for x in range(self.size**2-1):
            self.final_state.append(x+1)
        return self.final_state

    def getFreeSpot(self, current_state):
        i = 0
        for spot in current_state:
            if spot == " ":
                return i
            i += 1

    def translationFunction(self, state, direction):
        #To prevent mutability
        copy_state=state.copy()
        freePosition = self.getFreeSpot(copy_state)
        if direction == "u":
            # Saving the value that will be changing
            changingValue = copy_state[freePosition - self.size]
            # Setting the upper case to ' '
            copy_state[freePosition - self.size] = " "
            # Seetting the free spot to the value of the upper case
            copy_state[freePosition] = changingValue
            return copy_state

        if direction == "d":
            # Saving the value that will be changing
            changingValue = copy_state[freePosition + self.size]
            # Setting the bottom case to ' '
            copy_state[freePosition + self.size] = " "
            # Seetting the free spot to the value of the bottom case
            copy_state[freePosition] = changingValue
            return copy_state

        if direction == "l":
            # Saving the value that will be changing
            changingValue = copy_state[freePosition - 1]
            # Setting the left case to ' '
            copy_state[freePosition - 1] = " "
            # Seetting the free spot to the value of the left case
            copy_state[freePosition] = changingValue
            return copy_state

        if direction == "r":
            # Saving the value that will be changing
            changingValue = copy_state[freePosition + 1]
            # Setting the right case to ' '
            copy_state[freePosition + 1] = " "
            # Seetting the free spot to the value of the right case
            copy_state[freePosition] = changingValue
            return copy_state


    def setNextStates(self, current_state):
        freeSpotIndex = self.getFreeSpot(current_state)
        # If the free spot is on the upper ligne
        if freeSpotIndex < self.size:
            # If the empty spot is the upper left corner
            if freeSpotIndex == 0:
                self.next_states.append(
                    self.translationFunction(current_state, "r")
                )
                self.next_states.append(
                    self.translationFunction(current_state, "d")
                )
            # If the empty spot is the upper right corner
            elif freeSpotIndex == self.size-1:
                self.next_states.append(
                    self.translationFunction(current_state, "d")
                )
                self.next_states.append(
                    self.translationFunction(current_state, "l")
                )
            else:
                self.next_states.append(
                    self.translationFunction(current_state, "r")
                )
                self.next_states.append(
                    self.translationFunction(current_state, "l")
                )
                self.next_states.append(
                    self.translationFunction(current_state, "d")
                )


        # If the free spot is on the bottom ligne
        elif freeSpotIndex > self.size ** 2 - self.size -1:
            # If the empty spot is the bottom right corner
            if freeSpotIndex == self.size**2-1:
                self.next_states.append(
                    self.translationFunction(current_state, "u")
                )
                self.next_states.append(
                    self.translationFunction(current_state, "l")
                )
            # If the empty spot is the bottom left corner
            elif freeSpotIndex == self.size**2-self.size:
                self.next_states.append(
                    self.translationFunction(current_state, "u")
                )
                self.next_states.append(
                    self.translationFunction(current_state, "r")
                )
            else:
                self.next_states.append(
                    self.translationFunction(current_state, "u")
                )
                self.next_states.append(
                    self.translationFunction(current_state, "r")
                )
                self.next_states.append(
                    self.translationFunction(current_state, "l")
                )


        # If the free spot is on the left border but not in the corners
        elif freeSpotIndex%self.size==0:
            self.next_states.append(
                    self.translationFunction(current_state, "r")
                )
            self.next_states.append(
                self.translationFunction(current_state, "u")
            )
            self.next_states.append(
                self.translationFunction(current_state, "d")
            )

        # If the free spot is on the right border (the corners case is treated above)
        elif freeSpotIndex%self.size==2:
            self.next_states.append(
                    self.translationFunction(current_state, "l")
                )
            self.next_states.append(
                self.translationFunction(current_state, "u")
            )
            self.next_states.append(
                self.translationFunction(current_state, "d")
            )
        
        # If the free spot is not on any border
        else:
            self.next_states.append(
                    self.translationFunction(current_state, "u")
                )
            self.next_states.append(
                self.translationFunction(current_state, "d")
            )
            self.next_states.append(
                self.translationFunction(current_state, "l")
            )
            self.next_states.append(
                self.translationFunction(current_state, "r")
            )
        


state=State()
state.taquin_bfs()