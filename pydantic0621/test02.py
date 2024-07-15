import googlemaps

#將API憑證用以下指令包起來
gmaps=googlemaps.Client(key="AIzaSyBRJYD0VQMu2nPv7iko9ZAYRE4JoWAwKfo")

#簡單的調用資料示範
geocode_result = gmaps.geocode("臺北市")
geocode_result