# -*- coding: utf-8 -*-
"""生成 2026-10-10 法商小知识卡片"""
import json, os, shutil, re

BASE = os.path.dirname(os.path.abspath(__file__))
DATE = "2026-10-10"
TOPIC = "找个见证人，怎么就把遗嘱弄无效了？——民法典第 1140 条：谁不能当遗嘱见证人"

SEC1 = """<b>一、六种遗嘱形式，只有一种不需要见证人</b><br>
《民法典》第 1134—1139 条把遗嘱的形式定死为六种，其中四种都要求见证人在场：<br>
· <b>第 1134 条（自书遗嘱）</b>：自书遗嘱由遗嘱人亲笔书写，签名，注明年、月、日。——<span class="highlight">这是唯一不需要见证人的一种</span>。<br>
· <b>第 1135 条（代书遗嘱）</b>：应当有两个以上见证人在场见证，由其中一人代书，并由遗嘱人、代书人和其他见证人签名，注明年、月、日。<br>
· <b>第 1136 条（打印遗嘱）</b>：应当有两个以上见证人在场见证。遗嘱人和见证人应当在遗嘱<b>每一页</b>签名，注明年、月、日。<br>
· <b>第 1137 条（录音录像遗嘱）</b>：应当有两个以上见证人在场见证。遗嘱人和见证人应当在录音录像中记录其姓名或者肖像，以及年、月、日。<br>
· <b>第 1138 条（口头遗嘱）</b>：遗嘱人在危急情况下，可以立口头遗嘱。口头遗嘱应当有两个以上见证人在场见证。危急情况消除后，遗嘱人能够以书面或者录音录像形式立遗嘱的，所立的口头遗嘱无效。<br>
· <b>第 1139 条（公证遗嘱）</b>：公证遗嘱由遗嘱人经公证机构办理。<br><br>

<b>二、第 1140 条：三类人不能当见证人</b><br>
「下列人员不能作为遗嘱见证人：<br>
（一）无民事行为能力人、限制民事行为能力人以及<b>其他不具有见证能力的人</b>；<br>
（二）继承人、受遗赠人；<br>
（三）与继承人、受遗赠人有利害关系的人。」<br>
三项各管一件事：<b>第（一）项</b>管「有没有见证能力」——前两类按民事行为能力划分，后面还有一个兜底，比如代书遗嘱里不识字的人、盲人；录音录像或口头遗嘱里听不见的人；不通晓遗嘱人所用语言的人。<b>第（二）项</b>管「是不是直接利害人」——法定继承人（含第一顺序、第二顺序）、受遗赠人。<b>第（三）项</b>管「是不是间接利害人」。<br><br>

<b>三、解释（一）第 24 条：把「利害关系」写实</b><br>
《继承编解释（一）》（法释〔2020〕23 号）第 24 条：「继承人、受遗赠人的债权人、债务人，共同经营的合伙人，也应当视为与继承人、受遗赠人有利害关系，不能作为遗嘱的见证人。」<br>
这一条沿用的是原《继承法意见》第 36 条的口径。除法定列举之外，继承人、受遗赠人的配偶、近亲属通常也会被认定有利害关系（<span class="highlight">此为条文理解与司法实践口径，非条文原文</span>）。<br><br>

<b>四、最容易搞混的一点：「一家人都在场签字」恰恰最危险</b><br>
很多人以为，立遗嘱时把全家人叫齐、每个人都签个字最保险。事实正好相反——<br>
《民法典》第 1127 条：第一顺序继承人是配偶、子女、父母；第二顺序是兄弟姐妹、祖父母、外祖父母。这些人全部落在第 1140 条第（二）项的排除名单里。<br>
更关键的是：<span class="highlight">「不打算继承」也没用</span>。法律看的是身份，不是意愿。某位继承人当场表示放弃、或者说明「我一分不要」，他仍然是「继承人」，仍然不能当见证人。<br><br>

<b>五、「两个以上」怎么算</b><br>
第 1135—1138 条要求「两个以上见证人在场见证」。代书遗嘱里，<b>代书人本身就是见证人之一</b>——代书人加其他见证人合计两人以上即可，不是「代书人之外还要再来两个」。<br>
实务中更常见的建议是选 <b>3 人以上单数</b>，理由是见证人之间可以相互印证，减少事后陈述不一致的风险。<br><br>

<b>六、见证人不到位，遗嘱会怎样</b><br>
先说清楚一个分工：<b>第 1143 条</b>管的是另一类无效情形——「无民事行为能力人或者限制民事行为能力人所立的遗嘱无效。遗嘱必须表示遗嘱人的真实意思，受欺诈、胁迫所立的遗嘱无效。伪造的遗嘱无效。遗嘱被篡改的，篡改的内容无效。」这一条针对的是<b>遗嘱人</b>和<b>内容</b>。<br>
而见证人不符合第 1140 条，后果是<b>该遗嘱不具备法定形式要件，不产生遗嘱效力</b>；所涉遗产依<b>第 1154 条第（四）项</b>（遗嘱无效部分所涉及的遗产）按照法定继承办理。<br>
另外三条要一起看：<b>第 1142 条第 3 款</b>——「立有数份遗嘱，内容相抵触的，以最后的遗嘱为准」（公证遗嘱的优先效力已被删除）；<b>解释（一）第 28 条</b>——「遗嘱人立遗嘱时必须具有完全民事行为能力……遗嘱人立遗嘱时具有完全民事行为能力，后来成为无民事行为能力人或者限制民事行为能力人的，不影响遗嘱的效力」；<b>第 1141 条</b>——必留份，遗嘱应当为缺乏劳动能力又没有生活来源的继承人保留必要的遗产份额。<br>
公证遗嘱这边另有一套程序：《遗嘱公证细则》（2000 年 3 月 24 日司法部令第 57 号发布，自 2000 年 7 月 1 日起施行）<b>第 6 条</b>规定，遗嘱公证应当由两名公证人员共同办理，由其中一名公证员在公证书上署名；因特殊情况由一名公证员办理时，应当有一名见证人在场，见证人应当在遗嘱和笔录上签名。（该条援引的仍是已废止的《继承法》第十八条，现行对应条文是《民法典》第 1140 条。）"""

SEC2 = """<b>场景一：儿子当见证人——最典型的一种无效</b><br>
老人在家立代书遗嘱，把房子留给小儿子，让大儿子执笔，二女儿和邻居老李签字见证。<br>
结果：大儿子、二女儿都是法定继承人，依第 1140 条第（二）项不能当见证人；这份遗嘱只剩老李一个合格见证人，不满足「两个以上」的要求，形式要件不成立。<br>
只要在场签字的两位是继承人，无论谁执笔，这份遗嘱都站不住。<br><br>

<b>场景二：老伴当见证人——身份上就是第一顺序继承人</b><br>
最高人民检察院网站转载的一则检察机关普法案例（来源：《检察日报》）：「赵先生」的母亲经历过三段婚姻，最后一段是在养老院与一位老先生再婚。母亲去世后留有一份<b>打印遗嘱</b>，把房屋留给赵先生，见证人正是这位再婚丈夫。<br>
法院的结论是：老先生虽然不打算继承遗产，但在法律意义上属于遗嘱人的配偶，是第一顺序继承人，不能作为遗嘱见证人；该遗嘱因缺少符合法律规定的见证人，无法证实出于遗嘱人真实意思，最终被认定无效，房屋按法定继承处理。<br>
要点：<span class="highlight">不打算继承 ≠ 不是继承人</span>。身份在那里，就出局。<br><br>

<b>场景三：找「好兄弟」当见证人——第（三）项与解释（一）第 24 条</b><br>
老张是企业主，想请老朋友老王见证自己把公司股权留给儿子的遗嘱。但老王和老张的儿子合伙开另一家公司，两人之间还互相有借款。<br>
依解释（一）第 24 条，老王属于「继承人共同经营的合伙人／债权人／债务人」，视为有利害关系，不能当见证人。<br>
反过来同样成立：给继承人放贷的客户经理、欠继承人钱的生意伙伴、与继承人合伙的人、继承人的配偶和近亲属——都在这一项的范围里。选见证人之前先问一句：<b>他和我儿子、女儿有没有生意往来、借贷关系？</b><br><br>

<b>场景四：打印遗嘱「末页签个字」——每一页都要签</b><br>
打印遗嘱最大的坑是签名页数。<b>第 1136 条</b>要求「遗嘱人和见证人应当在遗嘱<b>每一页</b>签名，注明年、月、日」。三页纸只在最后一页签字，前面几页无法证明未被替换，形式要件不完整。<br>
同理，录音录像遗嘱（<b>第 1137 条</b>）必须在录像中记录姓名或者肖像，以及年、月、日；只录了内容、没录见证人身份和日期，同样有被认定不符合形式要件的风险。<br><br>

<b>场景五：口头遗嘱有「有效期」</b><br>
<b>第 1138 条</b>：口头遗嘱只在危急情况下可以立，且要有两个以上见证人在场；<span class="highlight">危急情况消除后，遗嘱人能够以书面或者录音录像形式立遗嘱的，所立的口头遗嘱无效</span>。<br>
所以口头遗嘱是「应急用」的，不是「长期用」的。危机一过，能补书面就赶紧补。<br><br>

<b>场景六：见证人「事后失能」要不要紧</b><br>
反过来不必担心：见证人是否合格，以<b>见证当时</b>的状态为准。见证时是完全民事行为能力人，之后因疾病丧失行为能力的，不影响该次见证的效力（此为条文理解与实务口径，非条文原文）。<br><br>

<b>场景七：那到底该找谁？</b><br>
· <b>可以找</b>：社区工作人员、村委会或居委会干部、邻居、朋友、原单位同事——与继承没有利害关系、能全程到场、能亲自签名、识字、听得清看得明。<br>
· <b>不能找</b>：任何法定继承人（含已表示放弃的）、受遗赠人、他们的配偶与近亲属、与继承人有债权债务或合伙关系的人、未成年人或不能辨认自己行为的人。<br>
· <b>必须全程在场</b>：从开始到签名，中途离开过就可能被质疑「没有全程见证」。<br>
· <b>最省事的替代方案</b>：去公证处办遗嘱公证（第 1139 条），由公证机构按《遗嘱公证细则》走程序，把「见证人找谁」这个坑直接在流程里消化掉。<br><br>

<b>场景八：保险这条「不需要见证人」的路</b><br>
保单指定受益人，法律没有要求见证人，也没有要求签字仪式：<br>
· 《保险法》<b>第 39 条</b>：人身保险的受益人由被保险人或者投保人指定；投保人指定受益人时须经被保险人同意。<br>
· <b>第 40 条</b>：可以指定一人或者数人为受益人，并可以确定<b>受益顺序和受益份额</b>；未确定受益份额的，受益人按照相等份额享有受益权。<br>
· <b>第 41 条</b>：变更受益人应当书面通知保险人，由保险人在保险单或者其他保险凭证上批注或者附贴批单。<br>
· <b>第 42 条</b>：只有在三种情形下保险金才<b>作为被保险人的遗产</b>——①没有指定受益人，或者受益人指定不明无法确定；②受益人先于被保险人死亡，没有其他受益人；③受益人依法丧失受益权或者放弃受益权，没有其他受益人。<br>
<span class="highlight">指定明确的受益人、又不落入第 42 条三种情形的身故保险金，不进遗产</span>——不走第 1154 条的回炉程序，也不需要全体继承人签字。遗嘱要跟「形式要件」一项一项较劲，保单只要把名字写对、把份额和顺位写清。"""

SEC3 = """⚠️ <b>见证人是「形式要件」，不是可选项。</b>代书（1135）、打印（1136）、录音录像（1137）、口头（1138）四种遗嘱都要求两个以上合格见证人。见证人不合格，等于形式要件缺一块，遗嘱不产生效力。<br>
⚠️ <b>继承人、受遗赠人一律不能当见证人——包括当场表示放弃的那位。</b>第 1140 条第（二）项看的是身份，不是意愿。配偶、子女、父母、兄弟姐妹、祖父母、外祖父母全在名单内。<br>
⚠️ <b>「利害关系」比想象的宽。</b>除第 1140 条第（三）项外，解释（一）第 24 条把继承人、受遗赠人的债权人、债务人、共同经营的合伙人一并划入。选见证人前，先核一遍他与继承人之间的生意、借贷、合伙关系。<br>
⚠️ <b>见证能力是事实判断，不是看年龄。</b>第 1140 条第（一）项还有「其他不具有见证能力的人」这个兜底：代书遗嘱里的不识字者、盲人，录音录像遗嘱里的失聪者，听不懂遗嘱人语言的人，都可能被认定不具有见证能力。<br>
⚠️ <b>「两个以上」算的是总人数。</b>第 1135 条里代书人本身就是见证人之一，不是「代书人之外再加两个」。但为了减少争议，实务上更建议选 3 人以上单数。<br>
⚠️ <b>打印遗嘱漏页签字，是最容易补救也最容易忽略的失误。</b>第 1136 条明确要求「每一页签名」并注明年、月、日——逐页签完、一次做完，别留半成品。<br>
⚠️ <b>见证人签名要用身份证上的名字。</b>用曾用名、笔名、小名，或者只按手印不签名，都会给遗嘱效力留下争议（此为实务口径）。<br>
⚠️ <b>口头遗嘱是应急工具，不是长期安排。</b>第 1138 条：危急情况消除后，遗嘱人能够以书面或者录音录像形式立遗嘱的，所立的口头遗嘱无效。<br>
⚠️ <b>遗嘱一旦被认定无效，遗产就回到法定继承。</b>依第 1154 条第（四）项，遗嘱无效部分所涉及的遗产按法定继承办理；配合第 1123 条的效力顺序（遗赠扶养协议 → 遗嘱 → 法定继承），一份写坏的遗嘱，等于什么都没写。<br>
✅ <b>动作一：立遗嘱前先列「排除名单」。</b>把全体法定继承人（含已放弃的）、受遗赠人，以及他们的配偶、近亲属、债权人、债务人、合伙人列出来——这些人都不能当见证人。<br>
✅ <b>动作二：见证人挑「三无人员」。</b>与继承无利害关系、能全程在场、能看清听懂并亲自签名——社区工作人员、村干部、邻居、朋友最合适。<br>
✅ <b>动作三：逐项对着条文核形式。</b>代书（1135）：两个以上见证人 + 代书人 + 全部签名 + 日期；打印（1136）：两个以上见证人 + 每一页签名 + 日期；录音录像（1137）：两个以上见证人 + 录像中记录姓名或肖像 + 日期；口头（1138）：仅限危急情况。<br>
✅ <b>动作四：嫌麻烦就走公证。</b>第 1139 条：公证遗嘱由遗嘱人经公证机构办理。由公证机构按《遗嘱公证细则》走程序，见证人资格的风险由公证环节消化。<br>
✅ <b>动作五：把钱的部分交给保单。</b>遗嘱的效力风险集中在「形式要件」，而保单指定受益人（《保险法》第 39—42 条）不需要见证人、不需要签字仪式，只要名字写对、份额顺位写清，保险金就直达受益人。<span class="highlight">物走遗嘱、钱走保单——让需要打官司的那部分尽量小，让确定给付的那部分尽量大。</span>"""

SUMMARY = "「找个见证人」这件事，法律管得比想象中细。《民法典》第 1134—1139 条规定了六种遗嘱形式：自书遗嘱（1134）由遗嘱人亲笔书写、签名、注明年月日，是<b>唯一不需要见证人</b>的一种；代书（1135）、打印（1136）、录音录像（1137）、口头（1138）四种都要求「两个以上见证人在场见证」，公证遗嘱（1139）由公证机构办理。第 1140 条列明三类人不能当见证人：①无民事行为能力人、限制民事行为能力人以及其他不具有见证能力的人；②继承人、受遗赠人；③与继承人、受遗赠人有利害关系的人——配套的《继承编解释（一）》（法释〔2020〕23 号）第 24 条进一步把继承人、受遗赠人的债权人、债务人、共同经营的合伙人划入「有利害关系」。最容易踩的两个坑：一是让配偶、子女当见证人（他们是第一顺序继承人，身份上就出局，当场表示放弃也不算）；二是打印遗嘱只在最后一页签字（第 1136 条要求<b>每一页</b>签名）。见证人不合格，遗嘱因不具备法定形式要件不产生效力，所涉遗产依第 1154 条第（四）项按法定继承办理——配合第 1142 条第 3 款「以最后的遗嘱为准」、解释（一）第 28 条「立遗嘱时须有完全民事行为能力」、第 1141 条必留份一起看，遗嘱的形式功课一点都省不掉。而《保险法》第 39—42 条给的是另一条路：指定受益人不需要见证人、不需要签字仪式，<span class=\"highlight\">指定明确、又不落入第 42 条三种情形的身故保险金不进遗产</span>，不走法定继承、不需全体继承人签字。物走遗嘱、钱走保单，是最省事的搭配。"

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

# 校验 index.html 与当日卡片逐字节一致
with open(card, encoding="utf-8") as f1, open(os.path.join(BASE, "index.html"), encoding="utf-8") as f2:
    assert f1.read() == f2.read(), "index.html != card"
print("index == card OK")
