function preload_document (next_doc)
{
	// Am I the "next document" or the "current document"?
	if (window . name == "preloader")
		// (next document)
		// Close the preloader window:
		self . close ();
	else
		// (current document)
		if (next_doc != null)
		{
			// Open a preloader window:
			window . open (next_doc, "preloader", "width=1,height=1");
			// Raise current window to the top:
			self . focus ();
		}
}