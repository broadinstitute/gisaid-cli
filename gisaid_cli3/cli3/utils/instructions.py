#!/usr/bin/env python3

"""
    Upload consensus sequences and metadata to GISAID's EpiCoV
    Copyright (C) 2022 Freunde von GISAID e.V.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pandas as pd
from cli3.utils.sequencers import SEQUENCERS
from io import StringIO


SEQUENCERS = pd.read_csv(StringIO(SEQUENCERS), header=None)
INSTRUCTIONS = {
"EpiCoV": {"Overview": """Fields marked by "**" are required. If a value is missing, use the term "unknown". Fields marked by "***" are required in full. Each row in the submission table is a sample record; each column is a variable.""",
"submitter***": "Your GISAID-registered email address",
"covv_virus_name***": """example hCoV-19/Country/SampleID/YYYY:
Let's break it down into the four parts delineated by the forward slash "/" character:
    - "hCoV-19": despite common usage of virus synonyms such as SARS-CoV-2 or nCoV-19, this first part must remain "hCoV-19" verbatim (to ensure backwards compatibility with EpiCoV db).
    - "Country" is full name of country of sample collection (e.g., Australia), including spaces. For backwards compatibility, the exception being to use "USA" for United States of America.
    - "SampleID" is recommended to be of the format, Loc-Lab-Number, where:
        - Loc is location abbreviation (use abbreviated state or province for location, such as "VIC" for Victoria, Australia, or "CA" for California, USA)
        - Lab is lab name abbreviation (e.g., "CDC" for Centres for Disease Control)
        - Number is sample number or lab code (e.g., 02978, or S47y)
    - "YYYY" is four digit year of sample collection. Note, this must be the same as the YYYY provided in the covv_collection_date value, else a "date inplausible" error will occur

    In this example, the covv_virus_name could be:
        - hCoV-19/Australia/VIC-CDC-02978/2022, or
        - hCoV-19/USA/CA-CDC-S47y/2022, respectively.

    NOTE: covv_virus_name field must match exactly the header of the respective sequence in the fasta file. This is the name key used to match up the sequence value in the sequence file.""",
"covv_type***": """For hCoV-19, this will always be "betacoronavirus".""",
"covv_passage**": """"Original" if the sample was sequenced directly from swabs, otherwise add the name of the cell line (e.g., "Vero") used to culture the specimen.""",
"covv_collection_date***": """Needs to be in the format "YYYY-MM-DD". Required in full.""",
"covv_location***": """Format as "Continent / Country / Region / Sub-region".""",
"covv_add_location": """Use this field to add additional location information. To add postcode or zipcode, add for example "other: postcode 3000".""",
"covv_host**": """For clinical samples, this is "Human". Otherwise add the species name of the organism from which the sample was originally sourced.""",
"covv_add_host_info": """Additional host information. E.g., include the EPI_ISL accession of the first sample in a longitudinal series, add patient co-morbidities, etc.""",
"covv_sampling_strategy": """Could be "longitudinal series" or for GISRS laboratories could be:
    - Sentinel surveillance (ILI),
    - Sentinel surveillance (ARI),
    - Sentinel surveillance (SARI),
    - Non-sentinel-surveillance (hospital),
    - Non-sentinel-surveillance (GP),
    - S gene dropout". """,
"covv_gender**": """Synonym for "Biological sex". Should be "Female", "Male", or "Other".""",
"covv_patient_age**": """Age in years of the person from whom the specimen was collected. May take format other than integer years, for example, "0.5" (i.e., 6 months), "5 days", "7 months". If units are not given, unit is assumed years, for example "35–44" or "35–39", "40–44".""",
"covv_patient_status**": """e.g., "Hospitalized", "Released", "Live", "Deceased". """,
"covv_specimen": """e.g., "Nasopharyngeal swab", "Sputum", "Bronchoalveolar lavage", "Mid-turbinate swab", "Alveolar lavage fluid", "Oropharyngeal swab", "Urine", "Stool", "Cloakal swab", "Organ", "Feces", "Other".""",
"covv_outbreak": """e.g., free text describing date, place, and/or family cluster.""",
"covv_last_vaccinated": """Important for vaccine breakthrough cases. Date and type of vaccination.""",
"covv_treatment": """e.g., Include drug name, dosage.""",
"covv_seq_technology**": "Add the sequencer brand and model.\n\n"+SEQUENCERS.to_csv(sep="\t", index=False, header=0),
"covv_assembly_method": """Freetext describing laboratory and bioinformatic pipeline in brief. For example, PCR primer sets, sequencing library kits and protocol, software and version numbers, reference genome accession against which variant sites were called, e.g. refseq EPI_ISL_402124, Illumina 250bp PE, ARTIC v4.1, minimap2 v2.22-r1101, samtools v1.13, iVar v1.3.1""",
"covv_coverage": """Average depth of coverage (i.e., average read depth) over the length of the reference genome. e.g., "3500x".""",
"covv_orig_lab***": """Full name of laboratory from where sample originated.""",
"covv_orig_lab_addr***": """Complete building address of laboratory from where sample originated.""",
"covv_provider_sample_id": """In-house sample-ID given by originating laboratory.""",
"covv_subm_lab***": """Full name of laboratory submitting this record to GISAID.""",
"covv_subm_lab_addr***": """Complete building address of the submitting laboratory.""",
"covv_subm_sample_id": """In-house sample-ID used by submitting laboratory.""",
"covv_authors***": """Complete list of authors who own the record (i.e., typically submitting and originating author lists combined)."""}
}
