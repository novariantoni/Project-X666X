import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))