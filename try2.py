import m3u8

playlist = m3u8.load('test.m3u8')
playlist.is_variant

print(playlist.segments)
print(playlist.target_duration)

# for playlist in playlist.playlists:
#     print(playlist.uri)
#     print(playlist.stream_info.bandwidth)

# print(playlist.dumps())

# if you want to write a file from its content

# playlist.dump('playlist.m3u8')