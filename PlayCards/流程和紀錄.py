# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-26
    Author: John Huang
'''

# 用案例討論
# 1. 有四個人在玩牌
# 2. 每回合都出一張牌，比大小，大的勝
# 3. 總共只有52張牌，一場有13回合
# 4. 一場當中只有一個人勝最多回合數，他就是該場勝者，如果有多人的話，就不算

# 5. 卡牌: 黑桃A > 方塊A ; 方塊A > 黑桃K  (先比數字大小，再比花色)
# 6. 一副牌: 52張，不重複 
# 7. 玩家: 拿牌、出牌
# 8. 莊家: 發牌、叫大家出牌、看誰出千、決定每回合勝者、叫紀錄記錄起來
# 9. 紀錄: 記錄每一回合勝者、計算回合數、公布本局勝者

# ====== 2022-07-28 ======
# 完成了Test Driven Development(測試驅動開發)的 CardTest.py 和 Card.py

# ====== 2022-07-29 ======
# 完成了Test Driven Development(測試驅動開發)的 DeckTest.py 和 Deck.py
# 完成了Test Driven Development(測試驅動開發)的 PlayerTest.py 和 Player.py
