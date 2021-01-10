# IMPORT HERE
import os
from colorama import init, Fore
init(autoreset=True)
# START WORKING HERE
askPermission = input("Wanna Create Project?(Y/N): ").lower()
if askPermission == 'y':
    project = str(input("Enter Directory Name: "))
    os.system(f'mkdir "{project}"')
else:
    project = "."
serverString = """\
//Server generated
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

// Routers Here
const index = require('./routers/index')

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.set('view engine', 'ejs')
app.use(express.static(`${__dirname}/statics`));

app.use('/', index)

const IP = process.env.IP || 'localhost'
const Port = process.env.PORT || 3000;

app.listen(Port, (err) => {
    if (err) {
       console.log(err)
   } else {
       console.log(`Server is Listening at http://${IP}:${Port}`);
    }
});
"""

filename = f"{project}\\server.js"
file = open(filename, 'w')
file.write(serverString)
file.close()

os.system(f'cd "{project}"&&npm init')
permissionPartTwo = str(input("Wanna Install Basic Modules: (Y/N(def.))")).lower()

if permissionPartTwo == 'y':
    print('Installing Basics Modules\n#1. express\n#2. body-parser\n#3. ejs')
    os.system(f'cd "{project}"&&npm install express body-parser ejs')
else:
    pass
print(Fore.MAGENTA+'Your main ejs files goes to "VIEWS" folder,\n\nFiles like CSS, JS, IMAGES goes to "STATICS" folder,\n\nRouters to "ROUTERS" folder\n\n')
os.system(f'cd "{project}"&&mkdir views&&mkdir statics&&mkdir routers')
os.system(f'mkdir "{project}"\\statics\\css')
os.system(f'mkdir "{project}"\\statics\\js')

indexHtmlFilePath = f"{project}\\views\\index.ejs"
indexHtml = open(indexHtmlFilePath, 'w')
indexHtml.close()

indexJSFilePath = f"{project}\\statics\\js\\app.js"
indexJS = open(indexJSFilePath, 'w')
indexJS.write('// Here lies your Main JS codes')
indexJS.close()

indexCSSFilePath = f"{project}\\statics\\css\\style.scss"
indexCSS = open(indexCSSFilePath, 'w')
indexCSS.write('// Here lies your Stylesheet')
indexCSS.close()

serverString = """\
const express = require('express');
const router = express.Router()

router.get('/', (req, res)=>{
    res.send(`<h1 style='color: green;'>Template is started Working</h1>`)
})

module.exports = router
"""

indexRouterFilePath = f"{project}\\routers\\index.js"
indexRouter = open(indexRouterFilePath, 'w')
indexRouter.write(serverString)
indexRouter.close()

print('BOILER PLATE GENERATED\n\nPress ENTER to continue\n\n'+ Fore.RED +'NOTE: SCREEN WILL BE CLEARED')


