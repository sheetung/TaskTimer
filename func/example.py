#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TaskTimer示例脚本

这个脚本是TaskTimer插件的示例，用于演示定时任务的执行。
脚本中有一个execute函数，会在定时任务触发时被调用。
"""

import time
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('TaskTimer-Example')


async def execute():
    """执行函数，会在定时任务触发时被调用
    
    Returns:
        str: 执行结果信息
    """
    # 获取当前时间
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    
    # 输出日志信息
    message = f"示例脚本执行于: {current_time}"
    logger.info(message)
    
    # 返回执行结果
    return message


if __name__ == '__main__':
    # 直接运行脚本时的测试代码
    import asyncio
    
    async def main():
        result = await execute()
        print(f"直接运行结果: {result}")
        
    asyncio.run(main())