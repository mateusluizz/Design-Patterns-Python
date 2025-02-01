class Gateway:
    def charge(self, amount: float) -> bool:
        if amount > 100:
            print("Payment authorized.")
            return True
        else:
            print("Payment declined.")
            return False
