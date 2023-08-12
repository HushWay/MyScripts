/*--------------------------------------------------------------
#' 提取基本信息与第一天的天气预报
--------------------------------------------------------------*/
function flatten(obj) {
    let result = {};
    for (let key in obj) {
        if (key === "forecast") {
            result = Object.assign(result, obj[key][0]); // 合并对象
        } else if (typeof obj[key] != "object") {
            result[key] = obj[key];
        }
    }
    return result;
}
const all_info = flatten($input.all()[0].json.data);


/*--------------------------------------------------------------
#' 获取指定的天气数据
--------------------------------------------------------------*/
function getWeather(all_info, mapped_keys) {
    let result = "";
    for (let key in mapped_keys) {
        console.log(key);
        let prefix = mapped_keys[key];
        if (prefix === "") {
            result += `${all_info[key]} \n`
        } else {
            result += `${prefix} ${all_info[key]} \n`
        }
    }
    return result;
}

const mapped_keys = {
    "type": "",
    "high": "",
    "low": "",
    "fx": "风向",
    "fl": "风力",
    "wendu": "当前温度",
    "shidu": "当前湿度",
    "quality": "空气质量",
};
const weather_info = getWeather(all_info, mapped_keys);

/*--------------------------------------------------------------
#' 今天会下雨吗？
--------------------------------------------------------------*/
const is_rainy = $input.all()[0].json.data.forecast[0].type.includes("雨");

/*--------------------------------------------------------------
#' 修改数据，返回结果
--------------------------------------------------------------*/
$input.all()[0].json["weather"] = weather_info;
$input.all()[0].json["is_rainy"] = is_rainy;

return $input.all();