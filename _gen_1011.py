# -*- coding: utf-8 -*-
"""生成 2026-10-11 法商小知识卡片（补档）"""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
DATE = "2026-10-11"
TOPIC = "谎称出险、故意撞车、小病大养——骗保的代价：《保险法》第 27 条，和它背后的《刑法》第 198 条"

SEC1 = """<b>一、先把两条最容易混的条文分开</b><br>
同样是「没说清」，法律上有两套完全不同的规则：<br>
· <b>《保险法》第 16 条</b>管的是<b>投保时</b>的如实告知义务——订立合同，保险人就保险标的或者被保险人的有关情况提出询问的，投保人应当如实告知。违反的，保险人可以解除合同，但受<b>第 16 条第 3 款「自合同成立之日起超过二年的，保险人不得解除合同」</b>（俗称不可抗辩）的限制。<br>
· <b>《保险法》第 27 条</b>管的是<b>事后造假</b>——没出险谎称出险、故意制造事故、伪造材料夸大损失。这是<b>故意骗取保险金</b>，性质完全不同。<br>
<span class="highlight">二年不可抗辩只锁第 16 条的告知瑕疵，管不到第 27 条的骗保。</span>这是本话题最高频的误读，先把这条界线划清。<br><br>

<b>二、第 27 条四款原文</b><br>
「未发生保险事故，被保险人或者受益人谎称发生了保险事故，向保险人提出赔偿或者给付保险金请求的，保险人有权解除合同，并不退还保险费。<br>
投保人、被保险人故意制造保险事故的，保险人有权解除合同，不承担赔偿或者给付保险金的责任；除本法第四十三条规定外，不退还保险费。<br>
保险事故发生后，投保人、被保险人或者受益人以伪造、变造的有关证明、资料或者其他证据，编造虚假的事故原因或者夸大损失程度的，保险人对其虚报的部分不承担赔偿或者给付保险金的责任。<br>
投保人、被保险人或者受益人有前三款规定行为之一，致使保险人支付保险金或者支出费用的，应当退回或者赔偿。」<br>
四款各管一件事：<b>第一款</b>——无中生有；<b>第二款</b>——自导自演；<b>第三款</b>——<span class="highlight">虚报的部分不赔，不是全案不赔</span>；<b>第四款</b>——拿到的要退回，花了保险公司的钱要赔。<br><br>

<b>三、第二款那句「除本法第四十三条规定外」是什么意思</b><br>
《保险法》<b>第 43 条第 1 款</b>：「投保人故意造成被保险人死亡、伤残或者疾病的，保险人不承担给付保险金的责任。投保人已交足二年以上保险费的，保险人应当按照合同约定向其他权利人退还保险单的现金价值。」<br>
也就是说：投保人故意制造的是<b>人身保险事故</b>（被保险人死亡、伤残、疾病）时，走第 43 条——<span class="highlight">不赔，但已交足二年以上保费的，现金价值要退给「其他权利人」，不是一律不退</span>。第 27 条第 2 款说的「除第 43 条外不退保费」，指的就是这个例外。<br>
第 43 条第 2 款另有一条：「受益人故意造成被保险人死亡、伤残、疾病的，或者故意杀害被保险人未遂的，该受益人丧失受益权。」——受益人下手的，这一份受益权直接归零，但其他受益人的权利不受影响。<br><br>

<b>四、行政责任：第 174 条</b><br>
「投保人、被保险人或者受益人有下列行为之一，进行保险诈骗活动，尚不构成犯罪的，依法给予行政处罚：（一）投保人故意虚构保险标的，骗取保险金的；（二）编造未曾发生的保险事故，或者编造虚假的事故原因或者夸大损失程度，骗取保险金的；（三）故意造成保险事故，骗取保险金的。」第 2 款把鉴定人、评估人、证明人一并纳入：故意提供虚假证明文件、为骗保提供条件的，同样处罚。<br>
所以「不构成犯罪」不等于没事——<span class="highlight">够不上刑事门槛的，还有行政处罚</span>。<br><br>

<b>五、刑事责任：《刑法》第 198 条保险诈骗罪</b><br>
五种情形：<b>（一）</b>投保人故意虚构保险标的，骗取保险金；<b>（二）</b>对发生的保险事故编造虚假的原因或者夸大损失的程度；<b>（三）</b>编造未曾发生的保险事故；<b>（四）</b>故意造成财产损失的保险事故；<b>（五）</b>故意造成被保险人死亡、伤残或者疾病。<br>
量刑三档：数额较大的，处五年以下有期徒刑或者拘役，并处一万元以上十万元以下罚金；数额巨大或者有其他严重情节的，处五年以上十年以下有期徒刑，并处二万元以上二十万元以下罚金；数额特别巨大或者有其他特别严重情节的，处十年以上有期徒刑，并处二万元以上二十万元以下罚金或者没收财产。<br>
两个加重装置：<b>第 2 款</b>——有第（四）（五）项行为，同时构成其他犯罪的，依照<b>数罪并罚</b>的规定处罚（故意杀人骗保、放火骗保，就是两罪并罚）；<b>第 4 款</b>——保险事故的鉴定人、证明人、财产评估人故意提供虚假的证明文件，为他人诈骗提供条件的，以<b>保险诈骗的共犯</b>论处。<br>
<b>立案追诉标准</b>：现行有效的是《最高人民检察院、公安部关于公安机关管辖的刑事案件立案追诉标准的规定（二）》（<b>2022 年 4 月 6 日修订</b>）<b>第 51 条</b>——进行保险诈骗活动，<span class="highlight">数额在五万元以上的，应予立案追诉</span>。（2010 年版第 56 条曾区分个人一万元、单位五万元，2022 年修订后统一为五万元。）<br><br>

<b>六、从业人员这一侧的红线：第 131 条</b><br>
《保险法》第 131 条列举保险代理人、保险经纪人及其从业人员在办理业务中的十项禁止行为，其中<b>第（九）项</b>直接点名——<span class="highlight">串通投保人、被保险人或者受益人，骗取保险金</span>。第（一）项「欺骗保险人、投保人、被保险人或者受益人」、第（六）项「伪造、擅自变更保险合同，或者为保险合同当事人提供虚假证明材料」也常与骗保勾连。违反的，依第 166 条由监管机构责令改正、处五万元以上三十万元以下罚款，情节严重的吊销业务许可证；构成犯罪的，依法追究刑事责任。<br>
<span class="highlight">业务员帮着造假，不是「帮客户」，是把自己也搭进去。</span>"""

SEC2 = """<b>场景一：没出险，硬说出险</b><br>
车没剐蹭，报一个「停在小区被撞、对方逃逸」，想走车损险补漆；或者家里水管没爆，报个「意外漏水」走家财险。<br>
依<b>第 27 条第 1 款</b>，保险人有权解除合同，<span class="highlight">并且不退还保险费</span>。这不是「补不补钱」的问题，是合同被解除、已交保费不退。<br><br>

<b>场景二：自己造一个事故出来</b><br>
「旧车想换新」故意把车开到树上；为了拿到高额身故金，先给家人投保再制造意外。<br>
依<b>第 27 条第 2 款</b>，解除合同、不赔、不退保费；如果造成的是被保险人死亡、伤残、疾病，还要叠加<b>第 43 条</b>（已交足二年以上的，现金价值退给其他权利人）。同时，这类行为大概率直接落入《刑法》<b>第 198 条第 1 款第（四）项或第（五）项</b>，并依第 2 款<b>数罪并罚</b>。<br>
<span class="highlight">「人财两空」在这里不是修辞，是结果</span>：保险金拿不到，还可能承担刑责。<br><br>

<b>场景三：小病大养、小修大赔——夸大损失</b><br>
住院单据上多挂几项检查、修车时把旧伤一起报进去、住院天数往后多写几天。<br>
<b>第 27 条第 3 款</b>的落点是「<b>对其虚报的部分</b>不承担赔偿或者给付保险金的责任」——真实损失该赔的仍要赔，虚报的部分不赔；如果已经领到手，依第 4 款<b>应当退回</b>。金额够大的，还可能触犯《刑法》第 198 条第 1 款第（二）项。<br>
很多人以为「只是多报一点点、不算骗保」，实际上定性看的是<b>是否故意虚构、虚报</b>，不是看金额是否「小」。<br><br>

<b>场景四：「熬过两年就没事了」是个危险的误读</b><br>
「不可抗辩」出自<b>第 16 条第 3 款</b>，原文是「自合同成立之日起超过二年的，保险人不得解除合同；发生保险事故的，保险人应当承担赔偿或者给付保险金的责任」。它解决的是<b>投保时的告知瑕疵</b>——比如投保时没提某项既往病史。<br>
而<b>第 27 条</b>针对的是<b>出险后的造假</b>，是故意骗赔，<span class="highlight">两条条文各管一段，第 16 条第 3 款的二年限制并不为第 27 条的骗保行为兜底</span>。把「两年」当成骗保的护身符，方向从一开始就错了。<br><br>

<b>场景五：业务员「帮忙想办法」</b><br>
客户出险后，代理人指导客户「病历上别写这个病」「就说是在家摔的」——这类「指导」，落在《保险法》<b>第 131 条第（一）项（欺骗）</b>、<b>第（九）项（串通骗取保险金）</b>上；情节严重的，构成《刑法》第 198 条保险诈骗罪的<b>共犯</b>。对代理人而言，执业资格、公司处分、刑事责任是三重风险。<br>
正确做法只有一条：如实提示客户按真实情况提交材料，把「能不能赔」交给核赔判断，不替客户设计事实。<br><br>

<b>场景六：出具假材料的第三方</b><br>
开假发票的、虚开诊断证明的、出具虚假车损评估的、帮人做伪证的鉴定人——<b>第 174 条第 2 款</b>把「鉴定人、评估人、证明人」列为可处罚对象；《刑法》<b>第 198 条第 4 款</b>更直接：故意提供虚假证明文件、为他人诈骗提供条件的，<b>以保险诈骗的共犯论处</b>。<br>
<span class="highlight">「我只是帮忙开个证明」不是挡箭牌。</span><br><br>

<b>场景七：正常理赔和骗保，界限在哪</b><br>
· 材料真实、损失真实，只是对<b>赔多少</b>有分歧——这是理赔争议，走协商、投诉、诉讼，不涉及第 27 条。<br>
· <b>编造</b>不存在的保险事故、<b>伪造变造</b>证明材料、<b>故意制造</b>事故——这才是第 27 条。<br>
· 判断的锚点是<b>主观故意 + 客观造假</b>：对事实的认识错误、表述不准、材料不全，不等于骗保。<br><br>

<b>场景八：把「赔得到」建立在合规上</b><br>
理赔顺利的前提是投保时如实告知（第 16 条）、出险后如实报案和提交真实材料（第 22 条）、对核定结果有异议走第 23—25 条和争议解决程序。<span class="highlight">所有「走捷径」的方案，终点都在第 27 条。</span>"""

SEC3 = """⚠️ <b>第 16 条 ≠ 第 27 条。</b>前者管「投保时没说清」（违反如实告知义务），后者管「出险后造假」（故意骗赔）。主张、抗辩、后果都不一样，先说错条文，方向就反了。<br>
⚠️ <b>「二年不可抗辩」不是骗保护身符。</b>第 16 条第 3 款的二年限制针对的是订立合同时的告知瑕疵，不能用来对抗第 27 条的骗保行为。<br>
⚠️ <b>夸大损失也可能入刑。</b>第 27 条第 3 款只是「虚报部分不赔」，但《刑法》第 198 条第 1 款第（二）项把「夸大损失程度骗取保险金」单独列为一种保险诈骗情形，不是「少报一点没关系」。<br>
⚠️ <b>第 27 条第 2 款有一个例外口子。</b>「除本法第四十三条规定外，不退还保险费」——投保人故意造成被保险人死亡、伤残、疾病的，已交足二年以上保费的，现金价值要退给其他权利人。别把「一律不退」说成绝对规则。<br>
⚠️ <b>故意制造事故往往是一案变两案。</b>《刑法》第 198 条第 2 款：有第（四）（五）项行为同时构成其他犯罪的，数罪并罚。放火、故意杀人、故意伤害，与保险诈骗罪一起算。<br>
⚠️ <b>立案追诉线是五万元。</b>依《立案追诉标准（二）》（2022 年修订）第 51 条，进行保险诈骗活动、数额在五万元以上的应予立案追诉。达不到刑事门槛的，还有第 174 条的行政处罚——<span class="highlight">不存在「数额不大就没事」</span>。<br>
⚠️ <b>不构成犯罪 ≠ 不用退钱。</b>第 27 条第 4 款：致使保险人支付保险金或者支出费用的，应当退回或者赔偿。这笔民事责任独立于行政、刑事责任存在。<br>
⚠️ <b>从业人员参与骗保是双罚。</b>第 131 条第（九）项「串通投保人、被保险人或者受益人，骗取保险金」是明令禁止行为；除行政处罚外，还可能被认定为保险诈骗罪的共犯。<br>
✅ <b>动作一：投保时如实告知。</b>问到什么答什么，把既往病史、职业、车辆使用性质等如实填——这是第 16 条项下最省事也最有效的做法，把第 16 条第 3 款之外的隐患一起消化掉。<br>
✅ <b>动作二：出险后只提交真实材料。</b>病历、票据、事故证明，一律按真实情况提供。缺材料可以补，造假补不回来。<br>
✅ <b>动作三：对理赔结果不满，走争议程序。</b>协商、向监管投诉、仲裁或诉讼——《保险法》第 23—26 条、第 30 条给的都是正规通道，不必绕到第 27 条上去。<br>
✅ <b>动作四：代理人守住一条线。</b>不替客户设计事实、不代签、不出具或转交虚假材料，如实告知客户「哪些能赔、哪些不能赔」。合规本身就是执业资格的保护。<br>
✅ <b>动作五：把理赔预期管理放在销售环节。</b>签单时把责任免除、等待期、如实告知的后果讲清楚，客户出险时的第一反应就不会是「想办法」。<span class="highlight">骗保的起点，往往是销售时没讲透的那几句话。</span>"""

SUMMARY = "骗保不是「理赔技巧」，是《保险法》和《刑法》双重规制的违法行为。《保险法》第 27 条分四款处理：①未发生保险事故谎称发生的，保险人有权解除合同并不退还保险费；②投保人、被保险人故意制造保险事故的，解除合同、不赔，除第 43 条规定外不退保险费；③以伪造、变造材料编造虚假事故原因或夸大损失程度的，保险人对<b>虚报的部分</b>不承担赔偿或者给付保险金的责任；④有前三款行为之一致使保险人支付保险金或支出费用的，应当退回或者赔偿。第 27 条第 2 款那句「除本法第四十三条规定外」，指的是投保人故意造成被保险人死亡、伤残、疾病时，已交足二年以上保费的，现金价值应退给其他权利人。行政责任见第 174 条（尚不构成犯罪的依法给予行政处罚），刑事责任见《刑法》第 198 条保险诈骗罪五种情形，最高可处十年以上有期徒刑；有第（四）（五）项行为同时构成其他犯罪的<b>数罪并罚</b>，鉴定人、证明人、财产评估人提供虚假证明文件的<b>以共犯论处</b>；立案追诉标准为《立案追诉标准（二）》（2022 年修订）第 51 条——数额在五万元以上。从业人员这一侧的红线在《保险法》第 131 条第（九）项：不得串通投保人、被保险人或者受益人骗取保险金。最需要说清的一条界线是：<span class=\"highlight\">「二年不可抗辩」出自第 16 条第 3 款，只管投保时的告知瑕疵，管不到第 27 条的骗保行为</span>——把两年当成骗保护身符，是方向性错误。理赔要赔得顺，靠的是投保如实告知、出险如实报案、材料真实完整，而不是事后「想办法」。"

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
for label, s in (("SEC1", SEC1), ("SEC2", SEC2), ("SEC3", SEC3), ("SUMMARY", SUMMARY)):
    plain = re.sub(r"<[^>]+>", "", s)
    assert '"' not in plain, "ASCII quote found in " + label
assert '"' not in TOPIC, "ASCII quote found in TOPIC"
print("quote-check OK")

# 复读校验 JSON 可解析
with open(dp, encoding="utf-8") as f:
    chk = json.load(f)
assert chk[-1]["date"] == DATE
assert len([d for d in chk if d["date"] == DATE]) == 1
print("json re-read OK, last =", chk[-1]["date"], "total =", len(chk))

# content_bank.json 回填（脚本抽取，不手抄）
bp = os.path.join(BASE, "content_bank.json")
with open(bp, encoding="utf-8") as f:
    bank = json.load(f)
bank = [b for b in bank if b.get("topic") != TOPIC]
bank.append({"topic": TOPIC, "law_points": SEC1, "practice_scene": SEC2,
             "risk_alert": SEC3, "summary": SUMMARY})
with open(bp, "w", encoding="utf-8") as f:
    json.dump(bank, f, ensure_ascii=False, indent=2)
print("content_bank.json ->", len(bank))
