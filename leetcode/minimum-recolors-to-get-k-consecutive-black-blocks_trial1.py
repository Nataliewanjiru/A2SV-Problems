class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_w = blocks[:k].count('W')
        min_w = current_w
        
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_w -= 1
            if blocks[i] == 'W':
                current_w += 1
            
            if current_w < min_w:
                min_w = current_w
                
        return min_w
