from messysoup.messysoup import *
from messysoup.table.table import *
import pytest


def test_a():
    assert a("test", href="test.domain") == "<a href=test.domain  >test</a>\n"

def test_abbreviation():
    assert abbreviation("test") == "<abbr >test</abbr>\n"

def test_address():
    assert address('test') == "<address >\ntest</address>\n"

def test_area():
    assert area() == "<area  >\n"

def test_article():
    assert article("test") == "<article >test</article>\n"

def test_aside():
    assert aside("test") == "<aside >test</aside>\n"

def test_audio():
    assert audio("test") == "<audio  >test</audio>\n"

def test_b():
    assert b("test") == "<b >test</b>\n"

def test_base():
    assert base('test') == "<base href=test   >\n"

def test_bdi():
    assert bdi("test") == "<bdi >test</bdi>\n"

def test_bdo():
    assert bdo("test", accesskey="test") == "<bdo  accesskey=test >test</bdo>\n"

def test_blockquote():
    assert blockquote("test") == "<blockquote  >test</blockquote>\n"

def test_body():
    assert body("test") == "<body >test</body>\n"

def test_br():
    assert br() == "<br>\n"

def test_button():
    assert button("test") == "<button  >test</button>\n"

def test_canvas():
    assert canvas("test") == "<canvas  >test</canvas>\n"

def test_caption():
    assert caption("test") == "<caption >test</caption>\n"

def test_cite():
    assert cite("test") == "<cite >test</cite>\n"

def test_code():
    assert code("test") == "<code >test</code>\n"

def test_col():
    assert col() == "<col   >\n"

def test_colgroup():
    assert colgroup("test") == "<colgroup  >test</colgroup>\n"

def test_data():
    assert data("test") == "<data  >test</data>\n"

def test_datalist():
    assert datalist("test") == "<datalist >test</datalist>\n"

def test_dd():
    assert dd("test") == "<dd >test</dd>\n"

def test_de():
    assert de("test") == "<del  >test</del>\n"

def test_details():
    assert details("test") == "<details  >test</details>\n"

def test_dfn():
    assert dfn("test") == "<dfn >test</dfn>\n"

def test_dialog():
    assert dialog("test") == "<dialog  >test</dialog>\n"

def test_div():
    assert div("test") == "<div >test</div>\n"

def test_dl():
    assert dl("test") == "<dl >test</dl>\n"

def test_dt():
    assert dt("test") == "<dt >test</dt>\n"

def test_em():
    assert em("test") == "<em >test</em>\n"

def test_fieldset():
    assert fieldset("test") == "<fieldset  >test</fieldset>\n"

def test_figcaption():
    assert figcaption("test") == "<figcaption >test</figcaption>\n"

def test_figure():
    assert figure("test") == "<figure >test</figure>\n"

def test_footer():
    assert footer("test") == "<footer >test</footer>\n"

def test_form():
    assert form("test") == "<form  >test</form>\n"

def test_h1():
    assert h1("test") == "<h1 >test</h1>\n"
    
def test_h2():
    assert h2("test") == "<h2 >test</h2>\n"
    
def test_h3():
    assert h3("test") == "<h3 >test</h3>\n"
    
def test_h4():
    assert h4("test") == "<h4 >test</h4>\n"
    
def test_h5():
    assert h5("test") == "<h5 >test</h5>\n"
    
def test_h6():
    assert h6("test") == "<h6 >test</h6>\n"

def test_head():
    assert head("test") == "<head >test</head>\n"

def test_header():
    assert header("test") == "<header >test</header>\n"

def test_hr():
    assert hr() == "<hr >\n"

def test_htlm():
    assert html("test") == "<html >test</html>\n"

def test_i():
    assert i("test") == "<i >test</i>\n"

def test_iframe():
    assert ifrmae("test") == "<iframe  >test</iframe>\n"

def test_img():
    assert img() == "<img  >\n"

def test_input():
    assert input_() == "<input  >\n"

def test_ins():
    assert ins("test") == "<ins  >test</ins>\n"

def test_kdb():
    assert kdb("test") == "<kdb >test</kdb>\n"

def test_label():
    assert label("test") == "<label  >test</label>\n"

def test_legend():
    assert legend("test") == "<legend >test</legend>\n"

def test_li():
    assert li("test") == "<li  >test</li>\n"

def test_link():
    assert link() == "<link  >\n"

def test_main():
    assert main("test") == "<main >test</main>\n"

def test_map_():
    assert map_("test") == "<map  >test</map>\n"

def test_mark():
    assert mark("test") == "<mark >test</mark>\n"

def test_meta():
    assert meta(charset="test") == "<meta charset=test  >\n"

def test_meter():
    assert meter("test") == "<meter  >test</meter>\n"

def test_nav():
    assert nav("test") == "<nav >test</nav>\n"

def test_noscript():
    assert noscript("test") == "<noscript >test</noscript>\n"

def test_ol():
    assert ol("test") == "<ol  >test</ol>\n"

def test_optgroup():
    assert optgroup("test") == "<optgroup  >test</optgroup>\n"

def test_option():
    assert option("test") == "<option  >test</option>\n"

def test_output():
    assert output("test") == "<output  >test</output>\n"

def test_p():
    assert p("test") == "<p >test</p>\n"

def test_param():
    assert param() == "<param  >\n"

def test_pre():
    assert pre("test") == "<pre >test</pre>\n"

def test_progress():
    assert progress("test") == "<progress  >test</progress>\n"

def test_q():
    assert q("test") == "<q  >test</q>\n"

def test_rp():
    assert rp("test") == "<rp >test</rp>\n"

def test_rt():
    assert rt("test") == "<rt >test</rt>\n"

def test_ruby():
    assert ruby("test") == "<ruby >test</ruby>\n"

def test_s():
    assert s("test") == "<s >test</s>\n"

def test_samp():
    assert samp("test") == "<samp >test</samp>\n"

def test_script():
    assert script("test") == "<script  >test</script>\n"

def test_section():
    assert section("test") == "<section >test</section>\n"

def test_select():
    assert select("test") == "<select  >test</select>\n"

def test_small():
    assert small("test")  == "<small >test</small>\n"

def test_source():
    assert source() == "<source  >\n"

def test_span():
    assert span("test") == "<span >test</span>\n"

def test_strong():
    assert strong("test") == "<strong >test</strong>\n"

def test_style():
    assert style("test") == "<style  >test</style>\n"

def test_sub():
    assert sub("test") == "<sub >test</sub>\n"

def test_summary():
    assert summary("test") == "<summary >test</summary>\n"

def test_sup():
    assert sup("test") == "<sup >test</sup>\n"

def test_svg():
    assert svg("test") == "<svg >test</svg>\n"

def test_table():
    assert table("test") == "<table >test</table>\n"

def test_tbody():
    assert tbody("test") == "<tbody >test</tbody>\n"

def test_td():
    assert td("test") == "<td  >test</td>\n"

def test_template():
    assert template("test") == "<template >test</template>\n"

def test_textarea():
    assert textarea("test") == "<textarea  >test</textarea>\n"

def test_tfoot():
    assert tfoot("test") == "<tfoot >test</tfoot>\n"

def test_th():
    assert th("test") == "<th  >test</th>\n"

def test_thead():
    assert thead("test") == "<thead >test</thead>\n"

def test_time():
    assert time("test") == "<time  >test</time>\n"

def test_title():
    assert title("test") == "<title >test</title>\n"

def test_tr():
    assert tr("test") == "<tr >test</tr>\n"

def test_u():
    assert u("test") == "<u >test</u>\n"

def test_ul():
    assert ul("test") == "<ul >test</ul>\n"

def test_var():
    assert var("test") == "<var >test</var>\n"

def test_video():
    assert video("test") == "<video  >test</video>\n"

def test_wbr():
    assert wbr("test") == "<wbr >test</wbr>\n"