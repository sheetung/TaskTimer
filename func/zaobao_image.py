import requests
import re

async def execute():
    # 目标 API 地址
    api_url = "https://zaobao.wpush.cn/api/zaobao/today"
    
    try:
        response = requests.get(api_url)
        # 检查请求是否成功
        if response.status_code == 200:
            # 解析 JSON 数据
            data = response.json()
            # 验证返回状态是否为 success
            if data.get("status") == "success":
                # 提取 image 链接
                image = data["data"].get("image")
                if image and image.startswith("http"):
                    return f"![早报图片]({image})"
                else:
                    print("未找到有效的 image 链接")
                    return "未找到有效的早报图片链接"
            else:
                print(f"API 返回失败：{data.get('message', '未知错误')}")
                return f"获取早报数据失败：{data.get('message', '未知错误')}"
        else:
            print(f"获取数据失败，状态码：{response.status_code}")
            return f"获取早报数据失败，状态码：{response.status_code}"
    except Exception as e:
        print(f"发生错误：{e}")
        return f"获取早报图片时发生错误：{str(e)}"

if __name__ == "__main__":
    import asyncio
    result = asyncio.run(execute())
    print(result)