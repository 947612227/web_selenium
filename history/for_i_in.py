
login = diver.find_elements_by_css_selector('div[id=u1] a[class=lb]')[0]
login.click()


user_str = ['9','4','7','6','1','2','2','2','7']
pass_str = ['z','h','a','n','g','J','I','A','0','.','.']

# print(len(user_str))
# print(len(pass_str))

user = diver.find_elements_by_id('TANGRAM__PSP_10__userName')[0]
user_str = ['9','4','7','6','1','2','2','2','7']
for i in user_str:
    user.send_keys(i)
    time.sleep(0.2)

password = diver.find_elements_by_id('TANGRAM__PSP_10__password')[0]
for j in pass_str:
    password.send_keys('z')
    time.sleep(0.2)

# user.send_keys('9')
# time.sleep(0.2)
# user.send_keys('4')
# time.sleep(0.2)
# user.send_keys('7')
# time.sleep(0.2)
# user.send_keys('6')
# time.sleep(0.2)
# user.send_keys('1')
# time.sleep(0.2)
# user.send_keys('2')
# time.sleep(0.2)
# user.send_keys('2')
# time.sleep(0.2)
# user.send_keys('2')
# time.sleep(0.2)
# user.send_keys('7')
# time.sleep(0.2)

# password.send_keys('z')
# time.sleep(0.2)
# password.send_keys('h')
# time.sleep(0.2)
# password.send_keys('a')
# time.sleep(0.2)
# password.send_keys('n')
# time.sleep(0.2)
# password.send_keys('g')
# time.sleep(0.2)
# password.send_keys('J')
# time.sleep(0.2)
# password.send_keys('I')
# time.sleep(0.2)
# password.send_keys('A')
# time.sleep(0.2)
# password.send_keys('0')
# time.sleep(0.2)
# password.send_keys('.')
# time.sleep(0.2)
# password.send_keys('.')
# time.sleep(0.2)