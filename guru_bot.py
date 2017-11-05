import stackexchange

def AskGuru(question):
    stackoverFlow = stackexchange.Site(stackexchange.StackOverflow)
    print("Asking: " + question)
    searchResults = stackoverFlow.search_advanced(
        pagesize=1,
        sort="relevance",
        q=question,
        accepted=True,
        page=1)

    if searchResults:
        result = searchResults[0]
        messageStart = "Does this help? : \n \n"
        return messageStart + result.title + "\n\t\t\t" + result.link + "\n"
    else:
        return "Sorry I cannot think of a good answer to that, try rephrasing that."
    