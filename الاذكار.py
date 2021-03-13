from plyer import notification
from time import sleep
at = ["سبحان الله" , "الحمدلله","الله اكبر","استغفر الله","سبحان الله وبحمده سبحان الله العظيم","لاحول ولاقوة الا بالله"]
for i in at:
    
    notification.notify(title= "الاذكار",
                        message= i,
                        app_icon = None,
                        timeout= 1,
                        toast=False)
    sleep(3600)
                    


