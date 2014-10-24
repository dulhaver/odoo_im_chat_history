this custom Module was built on top of OpenERP saas1 Instant Messaging [im] Module.
It has the purpose to add a menu "IM" where you get a list of all internal 
instant Messages between OpenERP users and can search them with standard OE Search. 
That works fine under OpenERP saas1.

NOTE: the "Instant Messaging" Module [im] by default stores all chat messages in the database 
already but it just does not provide a view to list and Search them. 
That is what this Module [im_history] adds to it.

Now we have switched to odoo 8.0 and the internal "Instant Messaging" (it's now called [im_chat]) 
still does not have the functionality of showing internal instant messages.
Only the more advanced [im_livechat] provides a messaging history. So, I want to port my 
saas1 module [im_history] to odoo 8.0 and call it [im_chat_history]

NOTE: I am not talking about [im_livechat] (which has a built-in messaging history for external chats 
as they come in for a support chat from a website for example)
