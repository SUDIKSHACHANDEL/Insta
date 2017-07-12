import requests
import urllib

String requestLikes = "https://api.instagram.com/v1/media/" + mediaID + "/likes?access_token=" + access_token + "&count=0";
        // Create a request for the URL.
        request = WebRequest.Create(requestLikes);
        // Get the response.
        response = request.GetResponse();
        //Remaining calls
        AddOrUpdateAppSettings("remainingCalls", response.Headers["X-Ratelimit-Remaining"]);
        // Display the status.
        Console.WriteLine(((HttpWebResponse)response).StatusDescription);
        // Get the stream containing content returned by the server.
        dataStream = response.GetResponseStream();
        // Open the stream using a StreamReader for easy access.
        reader = new StreamReader(dataStream);
        // Read the content.
        responseFromServer = reader.ReadToEnd();
