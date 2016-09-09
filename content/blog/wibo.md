Title: WIBO: Web Invoice Billing Organizer
Date: 2014-04-22 21:30
Author: Ben Sledge
Category: Projects
Tags: django, python
Slug: wibo
Status: published
Summary: Wibo was devaloped to be the ultimate print-shop job tracking and invoicing sytem. It combines kanban based ideas and advanced reporting to help managers and designers manage workloads and monitor the progress of an entire team.

**Wibo** was developed to be the ultimate print-shop job tracking and
invoicing system. It combines kanban based ideas and advanced reporting
to help managers and designers manage workloads and monitor the progress
of an entire team.

-   **Job Tracking:** The Job Queue provides an at-a-glance snapshot of
    who's working on what and when everything is due.
-   **Product Templating:** Product templates allows managers to save
    the production information for frequent jobs to reduce error on
    repeat orders.
-   **Automatic Billing:** Every Product carries all the pricing info
    needed to quote and bill jobs, so creating a quote or an invoice
    becomes a one-button operation.
-   **Waste Tracking:** Detailed waste reports help track exactly where
    efficiency needs to be improved.
-   **Agregated Reporting:** A Python based reporting system allows an
    unlimited varriaty of views in to production and cost data.

{% img {filename}/images/wibo_jobqueue.png 400 Wibo: Job Queue %}
{% img {filename}/images/wibo_newjob.png 400 Wibo: New Job Page %}<br />
{% img {filename}/images/wibo_invoices.png 400 Wibo: Invoice List %}
{% img {filename}/images/wibo_invoice.png 400 Wibo: Job Invoice %}


Technology
----------

Wibo is built on the Django framework for Python web development and is
accessed directly through a browser. On the front end, it uses Twitter's
Bootstap to create a familiar and responsive interface for users (that
works great on both desktops and mobile devices).

{% img {filename}/images/wibo_mobile_job.png 200 Wibo: Mobile Job Page %}
{% img {filename}/images/wibo_mobile_menu.png 200 Wibo: Mobile Menu %}
{% img {filename}/images/wibo_mobile_frequentjobs.png 200 Wibo: Mobile Frequent Jobs Page %}

I was the lead developer on the project from October 2012 until I
graduated from Clemson University in May 2014. Active development and
maintenance have been taken over by another developer. The current
source code can be viewed on [Campus Banner + Design's BitBucket
page](https://bitbucket.org/cbplusd/wibo/).
