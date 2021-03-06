import AddressSimilarity

compare = AddressSimilarity.addressSimilarity()
print (compare.compareChsAddress(u'香港島中西區摩星嶺1號', u'香港島中西區摩星嶺1號'))
print (compare.compareChsAddress(u'香港九龍元朗站3號客運大樓', u'九龍元朗站三號客運大樓'))
print (compare.compareChsAddress(u'九龍紅磡理工大學', u'九龍紅磡灣育才道11號'))
print (compare.compareChsAddress(u'新界沙田沙角街8號舖', u'沙田大圍沙角街八號'))
print (compare.compareChsAddress(u'香港新界老圍村一街1號3座地下', u'新界老圍村1街第3座地下'))
print (compare.compareChsAddress(u'旺角西洋菜南街一百九十號西洋大廈地下190-192B', u'香港九龍西洋菜街190號第190至192B號'))
print (compare.compareChsAddress(u'九龍尖沙咀寶勒巷五號30樓F室', u'九龍尖沙咀寶勒巷5號30F'))
print (compare.compareChsAddress(u'香港九龍深水埗深旺道1號巴士站', u'九龍彩虹巴士總站'))
print (compare.compareChsAddress(u'九龍尖沙咀寶勒巷10號10 PRAT 6樓', u'九龍尖沙咀寶勒巷10號寶勒10 6樓'))
print (compare.compareChsAddress(u'新界屯門海皇路海皇商場9樓902號舖', u'新界屯門V City 09樓902號'))
print (compare.compareChsAddress(u'香港島小西灣富欣花園商場地下1號', u'香港島銅鑼灣東角島一號地下'))
print (compare.compareChsAddress(u'新蒲崗錦榮街333號1號A - C', u'九龍新蒲崗康強街223號地下1A-1B號舖'))
print (compare.compareEngAddress(u'Mount Davis Bus Terminus, HK', u'Mount Davis Bus Terminus, HK'))
print (compare.compareEngAddress(u'No. 1, Mount Davis Bus Terminus, Hong Kong', u'No. 1, Mount Davis Bus Terminus'))
print (compare.compareEngAddress(u'11 Yuk Choi Rd, Hung Hom', u'No. 11, PolyU, Yuk Choi Road, Hung Hom, Kowloon'))
print (compare.compareEngAddress(u'1A, 1/F Fu Cheong Shopping Mall, Sham Mong Road, Sham Shui Po, HK', u'Shop 1A, Fu Cheong Shopping Mall, Fu Cheong Estate, Sham Shui Po, KLN'))
print (compare.compareEngAddress(u'ABERDEEN. G01-02, Port Centre, Aberdeen, Hong Kong', u'G01 - G02, G/F, Aberdeen Port Center, HK island, HK'))
print (compare.compareEngAddress(u'1/F, Yee Hing Building, No. 19 Leighton Road, Causeway Bay', u'Floor 1, YeeHing Building, 19 Leighton Road, Causeway Bay, Hong Kong'))
print (compare.compareEngAddress(u'Shop 119, 2/F, Kwai Chung Plaza, 7-11 Kwai Foo Road', u'No. 119, Floor 2, Kwai Chung Plaza, 7 - 11 Kwai Foo Rd., Kwai Chung, N.T.'))
print (compare.compareEngAddress(u'15/F., Sing Tao News Corporation Building, 3 Tung Wong Road, Shau Kei Wan, Hong Kong', u'1/F., 8 Chun Ying Street, Tseung Kwan O Industrial Estate West, N.T., Hong Kong'))
print (compare.compareEngAddress(u'Tin Shui Wai Station, Exit A, New Territories', u'Exit A, Tin Shui stn., NT'))
print (compare.compareEngAddress(u'3/F, Tung Che Commercial Centre, 246 Des Voeux Road West, Sai Ying Pun', u'7/F, To Kwa Wan Government Offices, 165 Ma Tau Wai Road, To Kwa Wan'))
print (compare.compareEngAddress(u'LG2, High Court, 38 Queensway, Hong Kong.', u'Shop 3E-08, Level 3 /F, Sunshine City Plaza, Ma On Shan, New Territories.'))
print (compare.compareEngAddress(u'Canossa Hospital (Caritas), 1 Old Peak Road', u'Caritas Medical Centre, 111 Wing Hong Street, Sham Shui Po'))

