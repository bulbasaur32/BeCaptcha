# BeCaptcha
Detection of Automated Software.

```python
"""
Used as decorator for callable ocject with async, captcha check runs in background.
Can be used in blocking-fashion, however is not recommended.

"""

@BeCaptcha
async def foo():

	await asyncio.sleep(3) # wait on process

	print('run code ...')

	await asyncio.sleep(3) # wait on process




passed_captcha, results = foo()
```
