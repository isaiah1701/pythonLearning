class Tempurature:
    def __init__(self,celsius):
        self.celsius=celsius 
    
    def to_farenheit(self) -> float :
        return self.celsius * 9 /5 +32

    def __str__(self) -> int:
        return f"{self.celsius}C ({self.to_farenheit()}F)"



London=Tempurature(32)
Tokyo=Tempurature(28)

print(str(London))
print(str(Tokyo))