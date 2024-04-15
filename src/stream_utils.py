def get_radio_stream_url(station_name):
    """
    Returns the stream URL for the given radio station name.
    """
    # Dictionary of radio stations and their stream URLs
    station_urls = {
        'jazz': 'http://example.com/stream/jazz',
        'rock': 'http://example.com/stream/rock',
        'classical': 'http://example.com/stream/classical',
        'pop': 'http://example.com/stream/pop',
        'bbc': 'http://stream.live.vc.bbcmedia.co.uk/bbc_world_service'
    }
    
    # Return the URL for the requested station or None if not found
    return station_urls.get(station_name.lower())
