import json
import datetime


class DataProcessor:
    
    def __init__(self, restaurant_data=None, users_data=None):
        self.restaurant_data = self._json_read(restaurant_data) if restaurant_data else []
        self.users_data = self._json_read(users_data) if users_data else []

    def process_users_data(self):
        for user in self.users_data:
            for item in user["purchaseHistory"]:
                item["transactionDate"] = item["transactionDate"].replace("/","-")
                temp = item["transactionDate"].split()
                date,time = temp[0],temp[1] + temp[2]
                d,m,y = date.split("-")
                date = y + "-" + m + "-" + d
                item["transactionDate"] = date + " " + DataProcessor._convert_to_24_hour(time)
        return self.users_data

    def process_restaurant_data(self):
        for res in self.restaurant_data:
            res["openingHours"] = DataProcessor._process_opening_hours(
                res["openingHours"])

        return self.restaurant_data

    @staticmethod
    def _json_read(file_path):
        with open(file_path) as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                exit()
        return data

    @staticmethod
    def _convert_to_24_hour(time_str):
        """Converts a time string in 12-hour format to 24-hour format"""
        time_str = time_str.lower()
        if "am" in time_str:
            time_str = time_str.replace("am", "")
            time_str = time_str.strip()
            if ":" in time_str:
                h, m = time_str.split(":")
                h, m = h.strip(), m.strip()
                h = int(h)
                return str(h)+":"+str(m)
            else:
                h = time_str.strip()
                h = int(h)
                return str(h)+":00"
        if "pm" in time_str:
            time_str = time_str.replace("pm","")
            time_str = time_str.strip()
            if ":" in time_str:
                h,m = time_str.split(":")
                h,m = h.strip(),m.strip()
                h = int(h)+12
                if h==24:
                    return "00:"+str(m)
                return str(h)+":"+str(m)
            else:
                h = time_str.strip()
                h = int(h)+12
                if h==24:
                    return "00:00"
                    
                return str(h)+":00"

    @staticmethod
    def _process_opening_hours(opening_hours_str):
        weekdays = {
            "Mon": 0, "Tues": 1, "Weds": 2, "Wed": 2, "Thurs": 3, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6
            }
        opening_hours = []
        time_slots = opening_hours_str.split(" / ")
        for time_slot in time_slots:
            weekindex = []
            for weekday in list(weekdays.keys()):
                if weekday in time_slot:
                    time_slot = time_slot.replace(weekday, "")
                    weekindex.append(weekdays[weekday])
            time_slot = time_slot.replace(",", "")
            time_slot = time_slot.strip()
            time_slot = time_slot.split("-")
            start_time, end_time = time_slot[-2], time_slot[-1]
            for idx in weekindex:
                opening_hours.append({
                    "day_of_week": idx,
                    "start_time": DataProcessor._convert_to_24_hour(start_time),
                    "end_time": DataProcessor._convert_to_24_hour(end_time)
                })
        return opening_hours
    
    

# # Example usage
# processor = DataProcessor("json_data/main_restaurant.json", "json_data/main_users.json")
# processed_restaurant_data = processor.process_restaurant_data()
# processed_users_data = processor.process_users_data()

