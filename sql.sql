Use 'lead_gen_business';

SELECT clients.first_name AS client_first_name, clients.last_name, sites.domain_name, leads.first_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id