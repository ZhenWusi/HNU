from RSA import generate_p_q_n, generate_rsa_keys, encrypt_message, decrypt_message
import random
# 生成Alice和Bob的公私钥对，使用相同的模数n
bits = int(input("请输入 p, q 的长度（例如：512 或 1024）: "))
p, q, n = generate_p_q_n(bits)
# Alice的公私钥
public_key_alice, private_key_alice = generate_rsa_keys(p, q, n)
e1, n = public_key_alice
d1, n = private_key_alice
print("Alice 公钥 e1:", e1)
print("Alice 私钥 d1:", d1)
# Bob的公私钥
public_key_bob, private_key_bob = generate_rsa_keys(p, q, n)
e2, n = public_key_bob
d2, n = private_key_bob
print("Bob 公钥 e2:", e2)
print("Bob 私钥 d2:", d2)
# 生成52张扑克牌的编号消息
cards = list(range(1, 53))
random.shuffle(cards)  # 任意顺序发送给Bob
print("ALice 生成的52个消息：", cards)
# 1. Alice生成52个消息并加密
encrypted_cards_alice = [encrypt_message(public_key_alice, card) for card in cards]
print("Alice 加密的牌:", encrypted_cards_alice)
# 2. Bob随机选取5张牌并用Bob的公钥加密发送给Alice
selected_indices_bob = random.sample(range(52), 5)
selected_encrypted_cards_bob = [encrypted_cards_alice[i] for i in selected_indices_bob]
print("Bob 选取的加密牌:", selected_encrypted_cards_bob)
encrypted_selected_cards_bob = [encrypt_message(public_key_bob, card) for card in selected_encrypted_cards_bob]
print("Bob 加密选取的加密牌:", encrypted_selected_cards_bob)
# 3. Alice用Alice私钥解密消息并回送给Bob
decrypted_selected_cards_alice = [decrypt_message(private_key_alice, card) for card in encrypted_selected_cards_bob]
print("Alice 解密后回送给Bob的牌:", decrypted_selected_cards_alice)
# 4. Bob用Bob私钥解密以确定他的一手牌
final_decrypted_cards_bob = [decrypt_message(private_key_bob, card) for card in decrypted_selected_cards_alice]
print("Bob 最终解密的牌:", final_decrypted_cards_bob)
# Bob选择另外5张牌发送给Alice
remaining_indices_bob = list(set(range(52)) - set(selected_indices_bob))
additional_selected_indices_bob = random.sample(remaining_indices_bob, 5)
additional_encrypted_cards_bob = [encrypted_cards_alice[i] for i in additional_selected_indices_bob]
# 5. Alice解密它们，变成她的一手牌
final_decrypted_cards_alice = [decrypt_message(private_key_alice, card) for card in additional_encrypted_cards_bob]
print("Alice 最终解密的牌:", final_decrypted_cards_alice)
# 游戏结束，Alice和Bob出示他们的牌和密钥对
print("Alice的密钥对:", private_key_alice)
print("Bob的密钥对:", private_key_bob)
# 验证双方牌是否正确
print("Alice 选取的牌:", final_decrypted_cards_alice)
print("Bob 选取的牌:", final_decrypted_cards_bob)
# 验证牌的合法性和正确性
# 验证 Bob 选取的5张牌通过 Alice 私钥解密后是否等于 Bob 最终解密的牌
bob_verification = all(decrypt_message(private_key_alice, encrypted_card) == card
                       for encrypted_card, card in zip(selected_encrypted_cards_bob, final_decrypted_cards_bob))
# 验证 Alice 用Bob的私钥解密 Bob 发送的牌是否在 Alice 最初的加密牌中
alice_verification = all(card in encrypted_cards_alice for card in (decrypt_message(private_key_bob,selected_cards_bob)for selected_cards_bob in encrypted_selected_cards_bob))
if bob_verification and alice_verification:
    print("双方验证成功，没有作弊行为。")
else:
    print("验证失败，存在作弊行为。")