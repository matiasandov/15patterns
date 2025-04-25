class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        - la longitud de la lista es: n + 1, es por eso que siempre hay espacio al menos para uno repetido
        - donde nums[i] puede ser cualquier numero de 1 a n
        - no puedes ordenar el array 

        Este es un problema de linked list por lo que cada nums[i] es un apuntador a un index
        - previous to beginning of cycle = distancia de intersección entre fast y slow hasta beginning of cycle
            1. Iniciar un slow_1 y un fast pointer
            2. recorrer la linked list hasta encontrar la primera intersección entre el slow_1 y el fast
            3. ahora te desharas del fast pointer, slow_1 se quedará en la intersección (en la imagen es 5) e iniciaras otro slow pointer (slow_2) al inicio de la listo
            4. como p = x, cuando slow_1 y slow_ 2 se intersecten este será el inicio de la lista
        """
        slow, fast = 0,0

        while True:
            #index de slow
            slow = nums[slow]
            #index de dos ponters adelante de slow -> asi es como avanzas dos lugares en la linked list
            fast = nums[nums[fast]]

            #si se interceptan
            if slow == fast:
                break
        
        slow_2 = 0
        
        while True:
            slow_2 = nums[slow_2]
            slow = nums[slow]

            if slow == slow_2:
                return slow
            

        



