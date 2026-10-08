# -*- coding: utf-8 -*-
"""生成 2026-10-08 法商小知识卡片"""
import json, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
DATE = "2026-10-08"
TOPIC = "爸妈留下一套房，三个孩子怎么分？——遗产「分不动」时的三层法律出路"
SUMMARY = "一套房、几个孩子，是继承里最常见也最容易伤感情的题。《民法典》给的规则链条是清晰的：<b>第 1121 条</b>继承自被继承人死亡时开始；<b>第 230 条</b>因继承取得物权自继承开始时发生效力——所以父母去世那一刻，房子在法律上已经属于全体继承人共有，登记只是确认；但<b>第 232 条</b>又规定处分这类不动产物权须登记才发生效力。份额算法是「<b>第 1153 条</b>先析产（共同财产先分一半给配偶）+ <b>第 1127 条</b>第一顺序（配偶、子女、父母）+ <b>第 1130 条</b>一般均等」——以「夫妻共同房产、父亲去世、妈妈加三个孩子、祖父母已故」为例，结果是<b>妈妈 5/8、三个孩子各 1/8</b>；最容易漏的是被继承人的父母和养子女、有扶养关系的继子女。分割的出路有三层：<b>第 1132 条</b>协商优先（份额也可协商不均等）、<b>第 1156 条</b>定方法（折价、适当补偿或者共有）、<b>第 303 条与第 304 条</b>谈不拢时请求分割（难以分割的可折价或拍卖、变卖后分价款）。过户端：<b>《不动产登记暂行条例》第 14 条</b>允许单方申请，<b>《实施细则》第 14 条</b>要求「全部法定继承人关于不动产分配的协议」或「经公证的材料／生效法律文书」，自然资源部已明确房产继承<b>无强制公证要求</b>，但「不强制公证」不等于「不需要所有人签字」。另有两条必须知道：<b>第 1157 条</b>——夫妻一方死亡后另一方再婚的，有权处分所继承的财产，任何人不得干涉，拿「不许再婚」卡过户没有法律依据；<b>第 301 条</b>——分割前擅自处分共有房产属无权处分，配合<b>第 311 条</b>善意取得规则，房子可能真追不回来。保险的对照价值在于「可分性」：《保险法》<b>第 39、40、41 条</b>允许指定受益人并确定受益顺序与份额，<b>第 42 条</b>只有三种情形保险金才作为遗产——<span class=\"highlight\">指定明确的受益人，身故保险金不进遗产、不进入分割程序</span>，房子解决「住」、保单解决「分」，这正是传承方案里最实用的一组搭配。"

SEC1 = """<b>一、继承从哪天开始？房子从哪天变成「大家的」？</b><br>
《民法典》第 1121 条：「继承从被继承人死亡时开始。相互有继承关系的数人在同一事件中死亡，难以确定死亡时间的，推定没有其他继承人的人先死亡。都有其他继承人，辈份不同的，推定长辈先死亡；辈份相同的，推定同时死亡，相互不发生继承。」<br>
第 1122 条：「遗产是自然人死亡时遗留的个人合法财产。依照法律规定或者根据其性质不得继承的遗产，不得继承。」<br>
关键在后面两条——第 230 条：「<span class="highlight">因继承取得物权的，自继承开始时发生效力</span>。」也就是说，父母去世的那一刻，房子在法律上<b>已经是全体继承人的共有物</b>，不动产登记只是「确认权利」，不是「产生权利」。<br>
紧接着是第 232 条：「处分依照本节规定享有的不动产物权，依照法律规定需要办理登记的，<span class="highlight">未经登记，不发生物权效力</span>。」——想卖、想抵押、想过户，必须先把登记办出来。权利是你的，但手续得走完。<br>
还有一条容易被忽略的《民法典》第 301 条：「处分共有的不动产或者动产以及对共有的不动产或者动产作重大修缮、变更性质或者用途的，应当经占份额三分之二以上的按份共有人或者<span class="highlight">全体共同共有人同意</span>，但是共有人之间另有约定的除外。」所以遗产分割前，任何一个继承人都不能单独把房子卖掉。<br><br>

<b>二、第一刀先给配偶：第 1153 条的「先析产、后继承」</b><br>
《民法典》第 1153 条：「夫妻共同所有的财产，除有约定的外，遗产分割时，应当先将共同所有的财产的一半分出为配偶所有，其余的为被继承人的遗产。遗产在家庭共有财产之中的，遗产分割时，应当先分出他人的财产。」<br>
第 1127 条：「遗产按照下列顺序继承：（一）第一顺序：配偶、子女、父母；（二）第二顺序：兄弟姐妹、祖父母、外祖父母。继承开始后，由第一顺序继承人继承，第二顺序继承人不继承；没有第一顺序继承人继承的，由第二顺序继承人继承。本编所称子女，包括婚生子女、非婚生子女、养子女和有扶养关系的继子女。……」<br>
第 1130 条：「同一顺序继承人继承遗产的份额，一般应当均等。……」<br>
把这三条连起来，就是一道最常见的算术题：<br>
· 房子是父母的夫妻共同财产，父亲去世，家里有妈妈 + 3 个孩子，爷爷奶奶已故；<br>
· 第一步（第 1153 条）：房子的一半先归妈妈，剩下 <b>1/2</b> 才是父亲的遗产；<br>
· 第二步（第 1127 条）：第一顺序继承人是妈妈 + 3 个孩子，共 4 人；<br>
· 第三步（第 1130 条）：这 1/2 由 4 人均分，每人 <b>1/8</b>；<br>
· 结果：<span class="highlight">妈妈合计 5/8，三个孩子各 1/8</span>。<br>
⚠️ 这里最容易漏的是两类人：①被继承人的<b>父母</b>（爷爷奶奶、外公外婆）也是第一顺序继承人，健在就要一起算；②<b>养子女、有扶养关系的继子女、非婚生子女</b>同样是「子女」（第 1127 条第 3 款）。少算一个人，后面所有份额全错。<br><br>

<b>三、「分不动」怎么办？法律给了三层解法</b><br>
<b>第一层：协商优先。</b>《民法典》第 1132 条：「继承人应当本着互谅互让、和睦团结的精神，协商处理继承问题。遗产分割的时间、办法和份额，由继承人协商确定；协商不成的，可以由人民调解委员会调解或者向人民法院提起诉讼。」<br>
注意：份额并非只能均等——第 1130 条最后一款：「继承人协商同意的，也可以不均等。」<span class="highlight">协商一致，比「一人一份」更有优先效力。</span><br>
<b>第二层：定「怎么分」。</b>第 1156 条：「遗产分割应当有利于生产和生活需要，不损害遗产的效用。<span class="highlight">不宜分割的遗产，可以采取折价、适当补偿或者共有等方法处理。</span>」<br>
一套房通常属于典型的「不宜分割」——切一半谁也住不了。所以落地方式基本就三种：<br>
· <b>折价</b>：一个人要房，按市场价把其他人的份额「买」下来；<br>
· <b>适当补偿</b>：房子归一方，给其他人金钱补偿；<br>
· <b>共有</b>：先共同登记，大家共有，暂不分。<br>
<b>第三层：谈不拢，就依法请求分割。</b>遗产分割前，继承人之间是共有关系（通说与审判实务口径：继承开始后、遗产分割前，遗产由全体继承人共同共有；《民法典》第 308 条：共有人对共有的不动产或者动产没有约定为按份共有或者共同共有，或者约定不明确的，除共有人具有家庭关系等外，视为按份共有）。<br>
《民法典》第 303 条：「共有人约定不得分割共有的不动产或者动产，以维持共有关系的，应当按照约定，但是共有人有重大理由需要分割的，可以请求分割；没有约定或者约定不明确的，按份共有人可以随时请求分割，<span class="highlight">共同共有人在共有的基础丧失或者有重大理由需要分割时可以请求分割</span>。因分割造成其他共有人损害的，应当给予赔偿。」<br>
第 304 条：「共有人可以协商确定分割方式。达不成协议，共有的不动产或者动产可以分割且不会因分割减损价值的，应当对实物予以分割；<span class="highlight">难以分割或者因分割会减损价值的，应当对折价或者拍卖、变卖取得的价款予以分割。</span>共有人分割所得的不动产或者动产有瑕疵的，其他共有人应当分担损失。」<br>
翻译一下：房子「难以分割」，法院可以判<b>折价补偿</b>，也可以判<b>拍卖、变卖后分钱</b>——这就是「分不动」的最终出口。<br><br>

<b>四、过不了「过户关」，一切停在纸面上</b><br>
· 《不动产登记暂行条例》第 14 条：继承、接受遗赠取得不动产权利的，可以由当事人<b>单方申请</b>登记。<br>
· 《不动产登记暂行条例实施细则》第 14 条：因继承、受遗赠取得不动产，当事人申请登记的，应当提交死亡证明材料、遗嘱或者<b>全部法定继承人关于不动产分配的协议</b>以及与被继承人的亲属关系材料等，也可以提交经公证的材料或者生效的法律文书。<br>
· 自然资源部在答复全国政协提案时明确：房产继承<b>并无强制公证要求</b>（原「继承房产应当持继承权公证书」的规定，随司法部废止《司法部、建设部关于房产登记管理中加强公证的联合通知》而取消），是否公证由当事人自行选择。<br>
但请注意：<span class="highlight">「不强制公证」不等于「不需要所有人配合」</span>。走「全部法定继承人关于不动产分配的协议」这条路，就意味着每一份签字都不能少；有一个人不签，就只能去法院拿一份生效法律文书。<br><br>

<b>五、有人拿条件卡签字：「你再婚，这房就没你份」</b><br>
《民法典》第 1157 条：「<span class="highlight">夫妻一方死亡后另一方再婚的，有权处分所继承的财产，任何组织或者个人不得干涉。</span>」<br>
所以「不许再婚才配合过户」这类条件，法律上站不住：再婚既不影响继承份额，也不影响处分权。<br>
反过来还有更隐蔽的一种卡法——要求对方「先签放弃继承声明」才肯配合办手续。要记住：放弃继承是<b>单方行为</b>，只要在遗产处理前、以书面形式作出（《民法典》第 1124 条），就产生法律效力。<span class="highlight">「被逼着签」的风险极大</span>，落笔之前一定要想清楚，别把「配合过户」的筹码，换成一张不可逆的放弃声明。"""

SEC2 = """<b>场景一：一套房、三个孩子、妈妈还在——先把算术做对</b><br>
父亲去世，房产是父母婚后共同购买，登记在父亲一人名下。很多人第一反应是「登记在爸爸名下，就是爸爸的遗产，四个人分」。<br>
错。依第 1153 条，先析出一半给妈妈；剩下 1/2 才是遗产，由妈妈 + 3 个孩子共 4 人均分（第 1127、1130 条）。<br>
<b>正确结果：妈妈 5/8，三个孩子各 1/8。</b><br>
如果爷爷奶奶还在世，他们也进第一顺序——那就变成 6 个人分那 1/2，每份 1/12。这也是很多家庭「谈着谈着发现份额对不上」的根源：一开始就漏了人。<br><br>

<b>场景二：老大要房、老二老三要钱——「折价补偿」怎么落地</b><br>
依第 1156 条，这是最常用、也最省事的方案：房子归老大，老大按份额给老二、老三钱。<br>
要写清楚的六件事：<br>
① <b>房子值多少</b>——先协商，协商不成做评估（评估费谁承担，一并约定）；<br>
② <b>给多少钱</b>——按份额 × 评估价算，写清总额和分期安排；<br>
③ <b>钱什么时候到</b>——建议「过户与付款同步」，避免「房过完了、钱没到」；<br>
④ <b>谁配合什么</b>——放弃继承声明、公证材料、过户签字的时间节点；<br>
⑤ <b>税费谁承担</b>——契税、个税、增值税等按实际发生约定清楚；<br>
⑥ <b>违约怎么办</b>——约定违约金和强制履行条款。<br>
如果房子里还住着人（比如妈妈），可以顺带把「居住」安排好：要么在协议里写明居住安排，要么依《民法典》第 366—371 条为老人<b>设立居住权并登记</b>——登记之后，房子过户了也赶不走人。<br><br>

<b>场景三：谁都不肯让——法院最后会怎么处理</b><br>
协商不成 → 人民调解委员会调解 → 起诉（第 1132 条）。法院的处理逻辑基本是第 1156 条 + 第 304 条：<br>
· 先看能不能实物分割（一套房基本不能）；<br>
· 再看能否折价补偿（谁出得起钱、谁更依赖这套房，往往是重要考量）；<br>
· 都不行，就拍卖、变卖，<b>分价款</b>。<br>
⚠️ 走到拍卖这一步，通常意味着「折价成交」——房子未必卖到理想价格，还要承担评估费、拍卖佣金、税费。这是「拖着不解决」最贵的结局。<br><br>

<b>场景四：有人卡着不签字，还拿「你再婚」当条件</b><br>
依第 1157 条，再婚是配偶的法定权利，任何人不得干涉；以「不许再婚」为条件拒绝配合过户，没有法律依据。<br>
但现实中的「卡」往往不是明着说的，而是「不签、不露面、不谈」。这时候有两条路：<br>
① 先固定证据——把协商过程、拒绝配合的事实留痕（微信记录、书面函件、调解记录）；<br>
② 起诉请求分割遗产。有了生效判决，依《不动产登记暂行条例》第 14 条与《实施细则》第 14 条，可以凭<b>生效法律文书</b>去办登记，不必再求人签字。<br><br>

<b>场景五：为什么保单是「天然分得动」的资产</b><br>
房子是「不可分」的实物，钱是「可分」的。这就是保单在传承里的位置——<br>
· 《保险法》第 39 条：人身保险的受益人由被保险人或者投保人指定；投保人指定受益人时须经被保险人同意。<br>
· 第 40 条：可以指定一人或者数人为受益人，并可以确定<b>受益顺序和受益份额</b>；未确定受益份额的，受益人按照相等份额享有受益权。<br>
· 第 41 条：变更受益人应当书面通知保险人，由保险人在保险单或者其他保险凭证上批注或者附贴批单。<br>
· 第 42 条：只有在三种情形下保险金才<b>作为被保险人的遗产</b>——①没有指定受益人，或者受益人指定不明无法确定；②受益人先于被保险人死亡，没有其他受益人；③受益人依法丧失受益权或者放弃受益权，没有其他受益人。<br>
<span class="highlight">指定了受益人、又不属于第 42 条三种情形的保险金，不进遗产</span>——它不需要「先析产、再继承、再协商、再评估、再拍卖」这一整套流程，保险公司按保单上写好的名字和份额给付，一分不多、一分不少。<br>
更实际的一层：很多家庭真正的问题不是「分不公」，而是<b>「房子只能给一个人，其他人拿不到钱」</b>。保单解决的正是这个缺口——<span class="highlight">房子给一个人，现金给其他人</span>，两样东西配在一起，才是能落地的方案。金额更大、情况更复杂时，还可以把保险金接入信托，按生前定好的规则分期、分条件给付。"""

SEC3 = """⚠️ <b>最容易漏的不是房子，是人。</b>第一顺序继承人是「配偶、子女、父母」（第 1127 条），被继承人的父母（爷爷奶奶、外公外婆）健在就要一起算；子女包括婚生子女、非婚生子女、养子女和有扶养关系的继子女。人漏一个，份额全错。<br>
⚠️ <b>「登记在谁名下就是谁的」是错的。</b>登记只产生权利推定效力。婚后取得的财产，即使只登记在一方名下，也先依第 1153 条析出一半给配偶，剩下才是遗产。<br>
⚠️ <b>「不强制公证」≠「不需要所有人配合」。</b>《不动产登记暂行条例实施细则》第 14 条给的是两条路：要么「全部法定继承人关于不动产分配的协议」，要么「经公证的材料或生效法律文书」。前者要所有人签字，后者要打官司。<br>
⚠️ <b>放弃继承声明不能随便签。</b>依《民法典》第 1124 条，遗产处理前、以书面形式作出的放弃，即为有效——签了就是签了，事后再想反悔，要由法院根据具体理由决定是否承认。<br>
⚠️ <b>分割前擅自卖房＝无权处分。</b>依第 301 条，处分共有不动产须经全体共同共有人同意；而依第 311 条，如果买家是善意的、付了合理价格、又办了登记，可能构成善意取得，房子就真追不回来了。<br>
⚠️ <b>「先拖一拖」不是办法，但也不必恐慌。</b>房子这类不动产，权利人请求返还财产<b>不适用诉讼时效</b>（《民法典》第 196 条第 2 项）；但如果是继承权被侵害、要求返还遗产份额，一般适用第 188 条的三年普通诉讼时效。<span class="highlight">这一层各地裁判口径并不完全一致，属实务口径而非统一规则</span>，具体情形请个案咨询。<br>
⚠️ <b>别把「共有」当成「分完了」。</b>共同登记只是把问题往后放：将来任何一方要变现，仍然要走第 303、304 条那条路，而且共有人之间还可能就处分、收益、费用产生新的纠纷。<br>
✅ <b>动作一：先画一张「继承人清单」。</b>配偶、子女（含婚生／非婚生／养／有扶养关系的继子女）、父母——一个都不能漏；有人已故的，再判断是否涉及代位继承（第 1128 条）或转继承（第 1152 条）。<br>
✅ <b>动作二：做一张「资产 + 负债」清单，并做评估。</b>房子、存款、理财、股权、车辆、保单；再减掉未还的贷款和债务（第 1159 条）。没有价格，就没有「折价补偿」的基础。<br>
✅ <b>动作三：分割协议要写全六件事。</b>谁要房、谁拿钱、多少钱、什么时候给、税费谁承担、违约怎么办——外加所有人的配合义务和时间节点。<br>
✅ <b>动作四：用「不进遗产的钱」解决「分不动」的房子。</b>人身保险指定明确受益人（《保险法》第 39、40、41 条），身故保险金不属于遗产、不进入分割程序；配置时回头检查三件事：<span class="highlight">受益人写清了吗？还在吗？有没有丧失或放弃受益权？</span>——这三问对应的正是第 42 条那三种会让保险金「变成遗产」的情形。房子解决「住」，保单解决「分」，两件事本来就该一起做。"""

TPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>法商小知识 - __DATE__</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background: #0a0a0a;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }
        .card {
            width: 375px;
            background: linear-gradient(180deg, #1a1a1a 0%, #0d0d0d 100%);
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
        }
        .header {
            background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
            padding: 24px 20px;
            text-align: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        .tag {
            font-size: 10px;
            color: rgba(255, 255, 255, 0.4);
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }
        .title {
            font-size: 32px;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 4px;
            margin-bottom: 4px;
        }
        .subtitle {
            font-size: 12px;
            color: rgba(255, 255, 255, 0.5);
            letter-spacing: 1px;
        }
        .content {
            padding: 24px 20px;
        }
        .topic {
            font-size: 16px;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 2px solid rgba(255, 255, 255, 0.1);
        }
        .section {
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 14px;
            font-weight: 600;
            color: #e8e8e8;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
        }
        .section-title::before {
            content: "";
            width: 4px;
            height: 16px;
            background: linear-gradient(180deg, #c9a96e 0%, #8b7355 100%);
            margin-right: 10px;
            border-radius: 2px;
        }
        .section-content {
            font-size: 13px;
            line-height: 1.8;
            color: rgba(255, 255, 255, 0.7);
            padding-left: 14px;
        }
        .highlight {
            color: #c9a96e;
            font-weight: 500;
        }
        .summary {
            background: rgba(201, 169, 110, 0.1);
            border-left: 3px solid #c9a96e;
            padding: 16px;
            margin-top: 24px;
            border-radius: 0 8px 8px 0;
        }
        .summary-title {
            font-size: 12px;
            color: #c9a96e;
            font-weight: 600;
            margin-bottom: 8px;
        }
        .summary-content {
            font-size: 13px;
            color: rgba(255, 255, 255, 0.8);
            line-height: 1.6;
        }
        .archive-banner {
            display: flex; align-items: center; gap: 8px;
            background: rgba(201,169,110,0.15);
            border-left: 4px solid #c9a96e;
            padding: 10px 20px; margin: 0 20px; border-radius: 0 8px 8px 0;
        }
        .archive-banner .ab-icon { font-size: 18px; }
        .archive-banner .ab-text { font-size: 12px; color: #c9a96e; font-weight: 600; }
        .archive-banner .ab-link { font-size: 12px; color: #c9a96e; font-weight: 700; text-decoration: underline; text-underline-offset: 3px; }
        .archive-banner .ab-link:hover { color: #fff; }
        .disclaimer {
            font-size: 9px;
            color: rgba(255, 255, 255, 0.3);
            padding: 12px 20px;
            line-height: 1.5;
            border-top: 1px solid rgba(255, 255, 255, 0.03);
        }
        @media print {
            body {
                background: #0a0a0a;
            }
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            <div class="tag">JUST INTERNAL INFORMATION</div>
            <div class="title">每日一条法商小知识</div>
        </div>

        <div class="content">
            <div class="archive-banner">
                <span class="ab-icon">📋</span>
                <span class="ab-text">往期回顾</span>
                <a class="ab-link" href="archive.html">点击查看全部历史 →</a>
            </div>
<div class="topic">__TOPIC__</div>

            <div class="section">
                <div class="section-title">法条要点</div>
                <div class="section-content">__SEC1__</div>
            </div>

            <div class="section">
                <div class="section-title">实务场景</div>
                <div class="section-content">__SEC2__</div>
            </div>

            <div class="section">
                <div class="section-title">风险提示</div>
                <div class="section-content">__SEC3__</div>
            </div>

<div class="summary">
                <div class="summary-title">核心要点</div>
                <div class="summary-content">__SUMMARY__</div>
            </div>
        </div>

        <div class="disclaimer">
            声明：本资讯内容仅供内部学习交流参考，不构成任何法律建议或投资建议。所涉观点或点评如非事实陈述，均为知识分享，不代表任何机构立场。任何决策请基于个人独立判断，并谨慎考虑自身实际情况。
            <br><br><a href="archive.html" style="color:rgba(255,255,255,0.2);text-decoration:none;font-size:10px;">历史回顾 →</a>
        </div>
    </div>
</body>
</html>
"""

html = (TPL.replace("__DATE__", DATE)
           .replace("__TOPIC__", TOPIC)
           .replace("__SEC1__", SEC1)
           .replace("__SEC2__", SEC2)
           .replace("__SEC3__", SEC3)
           .replace("__SUMMARY__", SUMMARY))

card = os.path.join(BASE, "fs_%s.html" % DATE)
with open(card, "w", encoding="utf-8") as f:
    f.write(html)
print("written:", card, len(html))

# index.html = 当日卡片逐字节复制
shutil.copyfile(card, os.path.join(BASE, "index.html"))
print("index.html copied from", os.path.basename(card))

# data.json 追加（同日去重）
dp = os.path.join(BASE, "data.json")
with open(dp, encoding="utf-8") as f:
    data = json.load(f)
before = len(data)
data = [d for d in data if d.get("date") != DATE]
data.append({"date": DATE, "topic": TOPIC, "summary": SUMMARY,
             "file": "fs_%s.html" % DATE})
data.sort(key=lambda x: x["date"])
with open(dp, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("data.json:", before, "->", len(data))

# 校验：正文与 summary 剥离标签后不得出现 ASCII 双引号
import re
for label, s in (("SEC1", SEC1), ("SEC2", SEC2), ("SEC3", SEC3), ("SUMMARY", SUMMARY)):
    plain = re.sub(r"<[^>]+>", "", s)
    assert '"' not in plain, "ASCII quote found in " + label
print("quote-check OK")

# 复读校验 JSON 可解析
with open(dp, encoding="utf-8") as f:
    chk = json.load(f)
assert chk[-1]["date"] == DATE
print("json re-read OK, last =", chk[-1]["date"], "total =", len(chk))
