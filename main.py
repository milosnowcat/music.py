#                      .                    .                           
#                 :-:--=:-:::.             :=-**##*=:                   
#                  :=----------.         .-%@@@@@@@@@%:                 
#                 :-------------:        :@@@@@@@@@@@@%.                
#                :-=-----------==:       +@@@@@@@@@@@@@#                
#              .------------=------.     =@@@@@@@@@@@@@#                
#               :=-=-------===-=--      .+%@@@@@@@@@@@#=                
#                --=--------==-=-.       -*%@@@@@@@@@*-.                
#                   ::----===+-             .#%@@@@*.                   
#                      -+++=: .               :+##+                     
#                     -+=====.              .=%@@%%%#=                  
#                  :-----------:.        :+#%%%@@@@@%@%+-               
#                -----------------      -%%%%%@@@%@@%%@%%*              
#               .-==----------==--:     #%%%@%@@@@@@@@@@%%.             
#               :-=+----------*=---    =%%%@@%%@@@%%@@@%%%=             
#               ---=----------*----:  .#%%%@@%%@@@%@%@@%%%%             
#              :-===----------+=---=  -#%%%@@%%@%@%@%@@%%%%=            
#                --=----------=#==+.   ==+%@@%%@@@%@%@@*++.             
#                --=-----------*=---  :===#@@%%@@@%@%%%--=              
#                -==-----------++--=  ---:#@%@@@%%%@@@%--=              
#                -=------------=:--=. =-- %@%%%%%%@%%%@=-=              
#               .-+-------------.:---.--: %%%%%%%%@%%@@+==              
#               :-++*++++++*+***. --=+--  *###########**-=              
#               --*+++++++++*+++: :--*-: :------=------*-=              
#               =-*++++++++*+***- .--*-. :-------------+-=              
#              .--*+++=+*++*+***+ :==*=: -------=------===:             
#              :=+++++==+++*++**+ -*++=. -------+-------+=:             
#               -++++=+==**+++***  :-:   -------+-------+.              
#                -+++=++=****+**#        -------+=------=               
#                .++==*=---=*+**+        =------+*------=               
#                 ----=    :---=          ====-.::+====                 
#            :**#==---=:   ----= ..   .:::=--=+*%#*--=+***. .--:..      
#            .=+**#=--==   :=--=%@*:.-=+%%*--=: ::+=--+***+=#@%*-=-::.  
#                :+=--=. :::=--=:.-*#%*--=*---+-+**=--=--=+**+*=**%@%=  
#                  =--= .#%%=--=.  +*#%#= +---#%++#=---.+%@%+  .+++*+-  
#                  ====   .:+===:   -==+= :===*+: -==== .--:.      ..   
#                  =--=     ----:         .----   :=---                 
#                  ----     :---:         .=---   .=---                 
#                  ----     :---:         .=---    =---                 
#                  ---:     :---:         .=---    +---                 
#                  +##%.    =*##-         -%%#:    %%%#                 
#                 :@@@@-    #@@@+         %@@@*   :@@@%:                
#                 .====.    -++=:         =+==-    --==.                

# @milosnowcat

import utils
import time

client_id = ""
client_secret = ""
redirect_uri = ""
username = ""
playlist_id = ""

playlist = utils.fetchPlaylist(client_id, client_secret, redirect_uri, username, playlist_id)

for song in playlist:
    time.sleep(1)
    print(song)
    utils.write("/play " + song)
