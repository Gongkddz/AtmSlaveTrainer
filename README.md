# ATM Slave Trainer

在BDSM关系中有一种叫做ATM奴，可以让M获得一种实质性的压迫，从而产生快感。本项目通过Python代码实现了一种游玩模式的仿真模拟，采用Tkinter库建立了简易的图形用户界面，方便上手。\
In BDSM relationships, there is a term called "ATM slave" that allows the submissive (M) to experience a form of
substantial oppression, resulting in pleasure. This project implements a simulation of a play mode using Python code and
creates a simple graphical user interface using the Tkinter library, making it easy to use.

## 仿真规则</br>Simulation Rules

1. 存款业务每次最低10元；</br>The minimum deposit amount for each transaction is 10 yuan.
1. 每次存款收取存款额50%的服务费；</br>A service fee of 50% of the deposit amount is charged for each deposit.
1. 每次存款成功与否的判定需要掷骰子，掷到1判定为存款成功，其他情况判定为存款失败，存款金额不计入账户也不退还；</br>The
   success of each deposit is determined by rolling a dice. Rolling a 1 is considered a successful deposit, while any
   other outcome is considered a failed deposit. Failed deposits do not count towards the account balance and are not
   refunded.

1. 用户可以选择再次缴纳服务费进行判定，直至判定为存款成功；</br>Users can choose to pay the service fee again for
   re-evaluation, until the deposit is considered successful.

1. 若用户放弃继续判定，则此次存款业务结束，存款金额和服务费均不退还；</br>If the user chooses to stop the re-evaluation,
   the deposit transaction ends, and both the deposit amount and service fee are not refunded.

1. 每日账户内的存款金额收取10%的利息；</br>Daily interest of 10% is applied to the deposit amount in the account.

1. 用户可以办理取款业务，银行随机在0-9之间生成一个校验码，用户在不知情的情况下输入一个校验码，若相同则取款成功，取款时收取50%的服务费；</br>
Users can perform withdrawal transactions. The bank generates a random verification code between 0 and 9. Users input a
verification code without knowing the generated code. If the codes match, the withdrawal is successful. A service fee of
50% is charged for withdrawals.

1. 用户可以选择再次缴纳服务费进行判定，直至判定为取款成功；</br>Users can choose to pay the service fee again for
   re-evaluation, until the withdrawal is considered successful.

1. 若用户放弃继续判定，则此次存取款务结束，账户内不会扣除取款金额，服务费不退还。</br>If the user chooses to stop the
   re-evaluation, the withdrawal transaction ends. The withdrawal amount is not deducted from the account, and the
   service fee is not refunded.

## 实现的功能</br>Implemented Features

1. 支持多用户的使用；</br>Support for multiple users.
1. 系统通过json保留每次操作记录；</br>System preserves each transaction record using JSON.
1. 系统启动时自动读取记录；</br>The system automatically loads the records when started.
1. 为用户提供基础的查询功能；</br>Basic query functionality
2. 基于Tkinter库的图形用户界面。</br>Graphical User Interface based on the Tkinter library.

## 项目用途说明</br>Project Purpose Description

1. 本项目可用于Python语言的学习。</br>This project can be used for learning Python language.
2. 本项目可用于游戏的仿真。</br>This project can be used for game simulation.
3. 本项目可独自使用。</br>This project can be used independently.
4. 其他用途必须遵守当地法规，符合社会公序良俗，并且基于当事人充分了解下的自愿原则。</br>Other uses must comply with local
   regulations, adhere to societal norms and ethics, and be based on the voluntary principle with a full understanding
   of the parties involved.

## 名词解释</br>Noun Definitions

1. BDSM（Bondage & Discipline, Dominance & Submission, Sadism &
   Masochism）是一种性取向、行为或约定，涵盖了封缚与训练、支配与服从、施虐与受虐等元素。在BDSM中，参与者通过讨论和约定来建立一种权力和控制的关系，其目的在于实现一个或多个参与者从中获得性满足、探索身体界限和实践互相尊重的安全环境。
   </br>BDSM (Bondage & Discipline, Dominance & Submission, Sadism & Masochism) is a sexual orientation, behavior, or
   agreement that encompasses elements of bondage and training, dominance and submission, and sadism and masochism. In
   BDSM, participants establish a power and control relationship through discussion and agreements, aiming to achieve
   sexual satisfaction, explore physical boundaries, and practice mutual respect in a safe environment.
2. ATM奴（ATM
   Slave）是在BDSM关系中的一种角色扮演，指的是一方以无偿给予其支配者财产、金钱或其他物品的方式来获得性快感和满足。这种行为通常需要在双方明确的同意和约定下进行，以确保安全、合法和双方的满意。ATM奴一般被视为一种财务奴役的形式，体现了权力和经济控制的关系。在这种关系中，支配者通常会设定财务目标和要求，而ATM奴则致力于履行这些要求并满足支配者的需求。这种行为在参与者之间是基于互相尊重、理解和明确约定的基础上进行的。
   </br>ATM Slave is a role-play within BDSM relationships, where one party derives sexual pleasure and satisfaction by
   voluntarily giving their dominator property, money, or other items without compensation. This behavior typically
   requires explicit consent and agreements between both parties to ensure safety, legality, and mutual satisfaction.
   ATM slavery is often viewed as a form of financial domination, reflecting power and economic control. In this
   dynamic, the dominator may set financial goals and requirements, while the ATM slave focuses on fulfilling these
   demands and satisfying the dominator's needs. This behavior is based on mutual respect, understanding, and clear
   agreements between participants.
3. 性癖（Paraphilia）是指一种特殊的性兴趣或性欲望，与传统的性行为、对象或方式不同。性癖经常与非常规或非常规的性幻想、行为或对象相关联。性癖是一种个体的心理特质，可能是出于它们对特定对象或行为的吸引、刺激、想象或满足。然而，对于一些性癖，参与者可能需要确保行为的合法性、同意性和安全性。
</br>Paraphilia refers to a specific sexual interest or desire that deviates from traditional sexual behaviors, objects,
or modes. Paraphilias are often associated with unconventional or non-normative sexual fantasies, behaviors, or objects.
Paraphilia is a psychological trait of an individual, driven by their attraction, stimulation, imagination, or
satisfaction with specific objects or behaviors. However, for some paraphilias, participants may need to ensure the
legality, consent, and safety.





