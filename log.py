import webbrowser

import fn.actions as fns
import fn.settings as set
import re
from fn.actions import *
from bs4 import BeautifulSoup as Soup
import traceback


def step_counter():
    step_counter.counter += 1
    return(step_counter.counter)
step_counter.counter = 0

def print_traceback():
    traceback.print_tb('', limit=None, file="/Users/natallia/PycharmProjects/mod/tstlog/cart01.txt")

class log (unittest.TestCase):

    def take_screenshot(step_name):
        sh_path = "/Users/natallia/PycharmProjects/mod/tstlog/" #Save screenshots into directory
        sh_name = re.sub(r'\W+', ' ', step_name)
        sh_name=sh_name.replace(" ", "_")
        save_sh_to=str(sh_path) + str(sh_name) + ".png"
        fns.actions.driver.find_element_by_tag_name('body').screenshot(save_sh_to)


#----------------------------------------------------------
# Create html file for test output at the start of a test


    global message
    def create_html_output(test_name, description):
        print("Test name: " + test_name)
        f = open('tstlog/'+test_name+'.html','w')
        message = """<html>
        <head> <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <title> Test Output: """+test_name+""" </title>
        <style>  .col-sm-1 {background-color: #dee2e2; color: #303131; font-size: 26px; text-align: center; width: 40px; height: 40px;
        margin-left: 20px; box-sizing: content-box; border: solid #20a19a 7px}
        .col-sm-9 { color: #303131; font-size: 21px; text-align: left; height: 40px; padding: 9px}
        .row {padding: 20px;}
        img{width: 80%; height: 80%; margin: 20px;}
        .failed_traceback, failed_xpath {color: #303131; font-size: 16px; text-align: left; margin-left: 10%;}
        #test_status, #failed_xpath {padding-left: 10%; font-size: 18px; background-color: #de4343;}
        
        </style>
        </head>
        <body style="background: linear-gradient(110deg, #dee2e2 60%, #ffffff 60% );">
            <nav class="navbar navbar-inverse" style=" ">
            <div class="container-fluid">
            <div class="navbar-header" style="background-image: linear-gradient(#26DCF5, #20a19a); width: 7%;">
            <p class="navbar-brand" style="color: black; margin: 0 5% 0 5%">"""+test_name+"""</p>
            </div>
            <div style="padding-top: 0.5%;color: #20a19a; font-size: 21px;text-align: center;">"""+description+"""</div>
            </div>
            </nav>
        <dev class="container-fluid" id="row0" style="margin: 0.5% 5% 0.5% 5%; font-size: 18px;"> </dev>
        </body>
        </html>   
        """
        f.write(message)
        f.close()

#---------------------------------------------------------------------------
# Add step name and screen shot for test step/action to the html output file

    def add_step(description, screen_shot):

        step_number=step_counter()
        prev_step=str(step_number-1)
        sv_path='/Users/natallia/PycharmProjects/mod/tstlog/'

        with open("/Users/natallia/PycharmProjects/mod/tstlog/cart01.html") as fp:
            soup = Soup(fp, 'html.parser')

        #Locationg existing dev tag
        tag = soup.find('dev', id='row'+prev_step)

        #Container: Creating new row
        newtag = soup.new_tag('dev', id='row'+str(step_number))
        newtag['class'] = "row"
        tag.insert_after(newtag)

        #Step number: Creating new div
        #Find parrent
        parent_tag = soup.find('dev', id='row'+str(step_number))

        #Create new
        num_tag = soup.new_tag("div", id="number "+ str(step_number))
        num_tag['class'] = "col-sm-1 step" + str(step_number)
        num_tag.string = str(step_number)
        parent_tag.append(num_tag)

        #Step description: Create new div
        #Locationg preceding div tag
        num_tagf = soup.find('div', id='number '+ str(step_number))

        #Container: Creating new dev tag
        desc_tag = soup.new_tag('div', id='step_description '+ str(step_number))
        desc_tag['class'] = "col-sm-9"
        desc_tag.string= description
        num_tagf.insert_after(desc_tag)

        if screen_shot =='y':
            sh_path = "/Users/natallia/PycharmProjects/mod/tstlog/" #Save screenshots into directory
            sh_name = re.sub(r'\W+', ' ', description)
            sh_name=sh_name.replace(" ", "_")
            save_sh_to=str(sh_path) + str(sh_name) + ".png"
            fns.driver.find_element_by_tag_name('body').screenshot(save_sh_to)

            #img
            decr_tagf = soup.find('div', id='step_description '+ str(step_number))
            img_tag = soup.new_tag('img', src=save_sh_to)
            decr_tagf.insert_after(img_tag)

        #Close file
        fp.close()
        #Make html pretty
        html = soup.prettify("utf-8")
        #Push Changes to html
        with open("/Users/natallia/PycharmProjects/mod/tstlog/cart01.html", "wb") as file:
            file.write(html)
        return step_number

#---------------------------------------------------------------------------
# Checkpoint (validation) : Add step name, actual and expected value to html output;
# Add screen shot if validation failed
# Highlight step number with orange color if validation failed

    def add_step_checkpoint(description, status, expectedv, actualv, screen_shot):

        #Step counter
        step_number=step_counter()
        prev_step=str(step_number-1)
        sv_path='/Users/natallia/PycharmProjects/mod/tstlog/'

        with open("/Users/natallia/PycharmProjects/mod/tstlog/cart01.html") as fp:
            soup = Soup(fp, 'html.parser')

        #Locationg existing dev tag
        tag = soup.find('dev', id='row'+prev_step)

        #Container: Creating new row
        newtag = soup.new_tag('dev', id='row'+str(step_number))
        newtag['class'] = "row"
        tag.insert_after(newtag)


        #Step number: Creating new div
        #Find parrent
        parent_tag = soup.find('dev', id='row'+str(step_number))


        #Create new
        num_tag = soup.new_tag("div", id="number "+ str(step_number))
        num_tag['class'] = "col-sm-1 step" + str(step_number)
        if status == 'fail':
            num_tag['style'] = "border: solid #fc5e03 7px"
        else:
            num_tag['style'] = "border: solid #20a19a 7px"
        num_tag.string = str(step_number)
        parent_tag.append(num_tag)


        #Step description: Create new div
        #Locationg preceding div tag
        num_tagf = soup.find('div', id='number '+ str(step_number))

        #Container: Creating new dev tag
        desc_tag = soup.new_tag('div', id='step_description '+ str(step_number))
        desc_tag['class'] = "col-sm-9"
        desc_tag.string= description
        num_tagf.insert_after(desc_tag)

        #Add assertion info
        decr_tagf1 = soup.find('div', id='step_description '+ str(step_number))

        #Expected text
        assert_tag_ex = soup.new_tag('p', id="assertex "+ str(step_number))
        assert_tag_ex['style'] = "margin-left: 10%; margin-top: 10px;"
        assert_tag_ex.string= "Expected value: " +expectedv
        decr_tagf1.insert_after(assert_tag_ex)
        #Actual text
        assert_tag_exf = soup.find('p', id='assertex '+ str(step_number))
        assert_tag_ac = soup.new_tag('p', id="assertac"+ str(step_number))
        assert_tag_ac['style'] = "margin-left: 10%;"
        assert_tag_ac.string= "Actual value: " +actualv
        assert_tag_exf.insert_after(assert_tag_ac)

        #Insert breaks
        br_tag=soup.new_tag('br')
        br_tag2=soup.new_tag('br')
        assert_tag_exf.insert_before(br_tag2)
        assert_tag_exf.insert_before(br_tag)

        if screen_shot =='y' or status == 'fail':
            sh_path = "/Users/natallia/PycharmProjects/mod/tstlog/" #Save screenshots into directory
            sh_name = re.sub(r'\W+', ' ', description)
            sh_name=sh_name.replace(" ", "_")
            save_sh_to=str(sh_path) + str(sh_name) + ".png"
            fns.driver.find_element_by_tag_name('body').screenshot(save_sh_to)

            #img
            decr_tagf = soup.find('p', id='assertac'+ str(step_number))
            img_tag = soup.new_tag('img', src=save_sh_to)
            img_tag['style'] ="padding-left:105px !important; width: 87%; height: 87%;"
            decr_tagf.insert_after(img_tag)

        #Close file
        fp.close()
        #Make html pretty
        html = soup.prettify("utf-8")
        #Push Changes to html
        with open("/Users/natallia/PycharmProjects/mod/tstlog/cart01.html", "wb") as file:
            file.write(html)
        return step_number





#-------------------------------------------------------------
# Exception handling
#-------------------------------------------------------------

    def exception_handle(xpathv_f, description):
        print ("Element not found and test failed")
        print('Xpath: ' + xpathv_f)
        trvar = traceback.extract_stack(None, 20)
        trace= traceback.format_list(trvar)

        # now your traceback is in the variable var
        print ('test', trace)

        #Add traceback to html output
        step_number=step_counter()
        prev_step=str(step_number-1)
        sv_path='/Users/natallia/PycharmProjects/mod/tstlog/'

        with open("/Users/natallia/PycharmProjects/mod/tstlog/cart01.html") as fp:
            soup = Soup(fp, 'html.parser')

        #Locationg existing dev tag
        tag = soup.find('dev', id='row'+prev_step)

        #Container: Creating new row
        newtag = soup.new_tag('dev', id='row'+str(step_number))
        newtag['class'] = "row"
        tag.insert_after(newtag)

        #Step number: Creating new div
        #Find parrent
        parent_tag = soup.find('dev', id='row'+str(step_number))

        #Create new
        num_tag = soup.new_tag("div", id="number "+ str(step_number))
        num_tag['class'] = "col-sm-1 step" + str(step_number)
        num_tag.string = str(step_number)
        parent_tag.append(num_tag)

        #Step description: Create new div
        #Locationg preceding div tag
        num_tagf = soup.find('div', id='number '+ str(step_number))

        #Container: Creating new dev tag
        desc_tag = soup.new_tag('div', id='step_description '+ str(step_number))
        desc_tag['class'] = "col-sm-9"
        desc_tag.string= description
        num_tagf.insert_after(desc_tag)

        #Take a screenshot
        sh_path = "/Users/natallia/PycharmProjects/mod/tstlog/" #Save screenshots into directory
        sh_name = re.sub(r'\W+', ' ', description)
        sh_name=sh_name.replace(" ", "_")
        save_sh_to=str(sh_path) + str(sh_name) + ".png"
        fns.driver.find_element_by_tag_name('body').screenshot(save_sh_to)

        #img
        decr_tagf = soup.find('div', id='step_description '+ str(step_number))
        img_tag = soup.new_tag('img', src=save_sh_to)
        img_tag['id'] = "fail"
        decr_tagf.insert_after(img_tag)
        br_tag=soup.new_tag('br')
        img_tag.insert_after(br_tag)
        img_tag.insert_after(br_tag)

        #Add test status (failed)
        failed_img= soup.find('img', id='fail')
        test_status=soup.new_tag('p', id='test_status')
        test_status.string='TEST FAILED'
        failed_img.insert_after(test_status)

        #Add failed xpath
        tst_status=soup.find('p', id='test_status')
        failed_xpath=soup.new_tag('p', id='failed_xpath')
        failed_xpath.string='Failed XPATH: ' + str(xpathv_f)
        tst_status.insert_after(failed_xpath)

        #Add traceback for failure
        c=0
        for i in trace:
            if c==0:
                failed_xp=soup.find('p', id='failed_xpath')
                failed_traceback=soup.new_tag('p', id='failed_traceback'+str(c))
                failed_traceback['class'] = "failed_traceback"
                failed_traceback.string=i
                failed_xp.insert_after(failed_traceback)
                c+=1
            else:
                failed_xp=soup.find('p', id='failed_traceback'+str(c-1))
                failed_traceback=soup.new_tag('p', id='failed_traceback' +str(c))
                failed_traceback['class'] = "failed_traceback"
                failed_traceback.string=i
                failed_xp.insert_after(failed_traceback)
                c+=1
        #Close file
        fp.close()
        #Make html pretty
        html = soup.prettify("utf-8")
        #Push Changes to html
        with open("/Users/natallia/PycharmProjects/mod/tstlog/cart01.html", "wb") as file:
            file.write(html)
        return step_number
