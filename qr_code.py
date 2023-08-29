import urllib.parse

from mad_hatter.decorators import tool


@tool(return_direct=True)
def create_qr_code(tool_input, bot):
	"""Replies to "qrcode xxx". Input is the data or url need to generate qr code."""

	encoded_data = urllib.parse.quote(tool_input)
	qr_code = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={encoded_data}"

	return f"![alt]({qr_code})"
