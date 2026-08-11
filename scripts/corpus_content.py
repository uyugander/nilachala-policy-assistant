"""
Synthetic policy content for Nilachala Textiles Pvt. Ltd.

This module contains ONLY data - no generation logic.
`scripts/generate_corpus.py` imports CORPUS from here and renders
each document to PDF or DOCX according to data/corpus_manifest.csv.

Structure of each document entry:
    {
        "title": str,
        "sections": [
            {"heading": str, "body": [str, ...]},          # paragraphs
            {"heading": str, "table": {                     # a real table
                "caption": str,
                "columns": [str, ...],
                "rows": [[str, ...], ...]
            }},
        ],
    }

DELIBERATE DATA CONFLICTS (do not "fix" these):
  - D01 states 12 casual / 18 earned leave  (current, v3.0)
  - D02 states 10 casual / 15 earned leave  (superseded, v1.0)
    These MUST disagree. They are the test case for version handling.
"""

FOOTER_NOTE = (
    "Nilachala Textiles Pvt. Ltd. - Internal document. "
    "Not for circulation outside the organisation."
)


CORPUS = {

    # ------------------------------------------------------------------
    # D01 - CURRENT leave policy (v3.0)
    # ------------------------------------------------------------------
    "D01": {
        "title": "Casual and Earned Leave Policy",
        "sections": [
            {
                "heading": "1. Purpose and Scope",
                "body": [
                    "This policy defines the leave entitlement available to all confirmed "
                    "employees of Nilachala Textiles Pvt. Ltd. and the procedure for "
                    "applying for and approving leave.",
                    "This policy applies to all permanent employees across all departments "
                    "and all locations. Contract staff, apprentices and trainees are covered "
                    "by separate arrangements described in their engagement letters.",
                    "This document supersedes the Leave Policy issued in 2019. Where any "
                    "conflict arises between this document and any earlier leave document, "
                    "the provisions of this document shall prevail.",
                ],
            },
            {
                "heading": "2. Leave Year",
                "body": [
                    "The leave year runs from 1 January to 31 December. Entitlement is "
                    "credited at the beginning of the leave year.",
                    "Employees joining part way through the leave year receive entitlement "
                    "on a pro-rata basis, calculated to the nearest half day.",
                ],
            },
            {
                "heading": "3. Leave Entitlement",
                "table": {
                    "caption": "Table 3.1 - Annual leave entitlement by category",
                    "columns": ["Leave type", "Days per year", "Carry forward", "Encashable"],
                    "rows": [
                        ["Casual leave", "12", "Not permitted", "No"],
                        ["Earned leave", "18", "Up to 30 days", "Yes, on separation"],
                        ["Sick leave", "10", "Not permitted", "No"],
                        ["Maternity leave", "182", "Not applicable", "No"],
                        ["Paternity leave", "15", "Not applicable", "No"],
                        ["Bereavement leave", "5", "Not applicable", "No"],
                    ],
                },
                "body": [
                    "Casual leave is intended for short, unforeseen absences and may be taken "
                    "for a maximum of three consecutive days at a time.",
                    "Earned leave accrues at one and a half days per completed month of "
                    "service. Unused earned leave may be carried forward to a maximum "
                    "accumulation of thirty days.",
                ],
            },
            {
                "heading": "4. Application Procedure",
                "body": [
                    "All leave must be applied for through the HR portal, or where portal "
                    "access is unavailable, by submitting Form HR-07 to the department head.",
                    "Casual leave should be applied for at least two working days in advance. "
                    "Earned leave of three days or more requires seven working days notice.",
                    "In case of sudden illness or emergency, the employee must inform their "
                    "reporting manager by telephone before the start of the shift and submit "
                    "a formal application within two working days of returning to work.",
                    "Leave is not considered granted until written approval is received. "
                    "Absence without approved leave is treated as unauthorised absence and "
                    "may attract disciplinary action under the Code of Conduct.",
                ],
            },
            {
                "heading": "5. Approval Authority",
                "table": {
                    "caption": "Table 5.1 - Approval authority by leave duration",
                    "columns": ["Duration", "Approving authority", "Notice required"],
                    "rows": [
                        ["Up to 2 days", "Reporting manager", "2 working days"],
                        ["3 to 7 days", "Department head", "7 working days"],
                        ["8 to 15 days", "Head of Operations", "15 working days"],
                        ["More than 15 days", "Managing Director", "30 working days"],
                    ],
                },
            },
            {
                "heading": "6. Sick Leave and Medical Certificate",
                "body": [
                    "Sick leave of three or more consecutive days must be supported by a "
                    "medical certificate from a registered medical practitioner.",
                    "The company reserves the right to require examination by a company "
                    "appointed physician where absence exceeds ten consecutive days.",
                ],
            },
            {
                "heading": "7. Leave During Notice Period",
                "body": [
                    "Employees serving notice may not take earned leave without the written "
                    "approval of the Head of Operations.",
                    "Any unused earned leave at the time of separation is encashed at basic "
                    "salary rate and paid with the final settlement.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D02 - SUPERSEDED leave policy (v1.0, 2019) - CONFLICTS WITH D01
    # ------------------------------------------------------------------
    "D02": {
        "title": "Leave Policy",
        "sections": [
            {
                "heading": "1. Introduction",
                "body": [
                    "This policy sets out the leave entitlement for employees of Nilachala "
                    "Textiles Pvt. Ltd. with effect from 1 April 2019.",
                    "This policy applies to all permanent employees who have completed their "
                    "probation period of six months.",
                ],
            },
            {
                "heading": "2. Entitlement",
                "table": {
                    "caption": "Table 2.1 - Leave entitlement",
                    "columns": ["Leave type", "Days per year", "Carry forward"],
                    "rows": [
                        ["Casual leave", "10", "Not permitted"],
                        ["Earned leave", "15", "Up to 20 days"],
                        ["Sick leave", "7", "Not permitted"],
                        ["Maternity leave", "182", "Not applicable"],
                    ],
                },
                "body": [
                    "Casual leave may be taken for a maximum of two consecutive days.",
                    "Earned leave accrues at one and a quarter days per completed month of "
                    "service, subject to a maximum accumulation of twenty days.",
                ],
            },
            {
                "heading": "3. Application",
                "body": [
                    "Leave applications are to be submitted in writing to the department head "
                    "using Form HR-07 at least three working days in advance.",
                    "Paternity leave is not provided under this policy.",
                ],
            },
            {
                "heading": "4. Approval",
                "body": [
                    "Leave of up to five days may be approved by the department head. Leave "
                    "exceeding five days requires approval from the Managing Director.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D03 - Employee Handbook (long document, ~94 pages after expansion)
    # ------------------------------------------------------------------
    "D03": {
        "title": "Employee Handbook",
        "sections": [
            {
                "heading": "1. Welcome to Nilachala Textiles",
                "body": [
                    "Nilachala Textiles Pvt. Ltd. was established in 1987 in Bhubaneswar and "
                    "today employs approximately four hundred people across manufacturing, "
                    "quality control, logistics and administration.",
                    "This handbook is provided to every employee on joining. It summarises "
                    "the terms of employment, workplace expectations and the principal "
                    "policies of the company. Where this handbook summarises a policy that "
                    "is described in full in a separate document, the separate document "
                    "prevails.",
                ],
            },
            {
                "heading": "2. Working Hours and Attendance",
                "body": [
                    "The standard working week is forty eight hours, worked over six days "
                    "from Monday to Saturday.",
                    "Office staff work from 9:30 am to 6:00 pm with a forty five minute "
                    "lunch break. Production staff work in shifts as set out below.",
                    "Attendance is recorded through the biometric system at the main gate. "
                    "Employees must record both entry and exit. Failure to record exit is "
                    "treated as absence for that day unless corrected within two working days.",
                ],
            },
            {
                "heading": "3. Shift Timings",
                "table": {
                    "caption": "Table 3.1 - Production shift schedule",
                    "columns": ["Shift", "Timing", "Break", "Shift allowance"],
                    "rows": [
                        ["General", "9:00 am - 5:30 pm", "45 min", "Nil"],
                        ["Shift A", "6:00 am - 2:00 pm", "30 min", "Rs. 40 per shift"],
                        ["Shift B", "2:00 pm - 10:00 pm", "30 min", "Rs. 60 per shift"],
                        ["Shift C", "10:00 pm - 6:00 am", "30 min", "Rs. 120 per shift"],
                    ],
                },
                "body": [
                    "Shift rosters are published on the notice board by the twenty fifth of "
                    "the preceding month. Requests for shift changes must be made to the "
                    "production supervisor at least seven days in advance.",
                    "No employee may work two consecutive full shifts.",
                ],
            },
            {
                "heading": "4. Probation and Confirmation",
                "body": [
                    "All new employees serve a probation period of six months. Probation may "
                    "be extended once by a maximum of three months where performance requires "
                    "further assessment.",
                    "Confirmation is issued in writing following a review by the reporting "
                    "manager and the HR department. Employees on probation are entitled to "
                    "sick leave but not to casual or earned leave.",
                ],
            },
            {
                "heading": "5. Compensation and Payroll",
                "body": [
                    "Salary is credited on or before the seventh day of the following month "
                    "to the employee's registered bank account.",
                    "Salary slips are made available through the HR portal by the tenth of "
                    "each month. Employees requiring a physical copy may request one from "
                    "the HR department.",
                    "Queries regarding individual salary calculation, deductions or bank "
                    "credit should be raised with the payroll executive in the Finance "
                    "department. The HR helpdesk does not handle individual salary queries.",
                ],
            },
            {
                "heading": "6. Statutory Deductions",
                "table": {
                    "caption": "Table 6.1 - Standard statutory deductions",
                    "columns": ["Deduction", "Employee share", "Employer share", "Applicability"],
                    "rows": [
                        ["Provident Fund", "12% of basic", "12% of basic", "All employees"],
                        ["ESI", "0.75% of gross", "3.25% of gross", "Gross up to Rs. 21,000"],
                        ["Professional Tax", "As per Odisha slab", "Nil", "All employees"],
                        ["Income Tax", "As per declaration", "Nil", "As applicable"],
                    ],
                },
            },
            {
                "heading": "7. Dress Code and Identity Cards",
                "body": [
                    "Production staff must wear the issued uniform and safety footwear at all "
                    "times on the factory floor. Office staff are expected to dress in formal "
                    "or smart casual attire.",
                    "Identity cards must be worn visibly at all times within company premises. "
                    "Loss of an identity card must be reported to the security office "
                    "immediately. A replacement fee of Rs. 200 applies.",
                ],
            },
            {
                "heading": "8. Use of Company Property",
                "body": [
                    "Company property including tools, vehicles, computers and communication "
                    "equipment is provided for business use. Limited personal use of "
                    "computers and internet is permitted provided it does not interfere with "
                    "work or breach the IT policy.",
                    "Employees are responsible for the safe custody of property issued to "
                    "them and must report loss or damage immediately.",
                ],
            },
            {
                "heading": "9. Performance Review",
                "body": [
                    "Performance reviews are conducted annually in March. Ratings are "
                    "discussed between the employee and the reporting manager before being "
                    "finalised.",
                    "Increments, where applicable, take effect from 1 April and are "
                    "communicated in writing by the Finance department.",
                ],
            },
            {
                "heading": "10. Grievance Redressal",
                "body": [
                    "An employee with a workplace grievance should first raise it with their "
                    "reporting manager. If unresolved within seven working days, the matter "
                    "may be escalated in writing to the HR department.",
                    "Grievances relating to harassment, discrimination or safety may be "
                    "raised directly with the HR department or the Internal Committee without "
                    "involving the reporting manager.",
                    "The HR helpdesk is available on extension 204 between 10:00 am and "
                    "5:00 pm on working days.",
                ],
            },
            {
                "heading": "11. Separation",
                "body": [
                    "Employees wishing to resign must give notice as specified in their "
                    "appointment letter, normally thirty days for staff and sixty days for "
                    "management grades.",
                    "On the last working day the employee must return all company property "
                    "and complete the clearance form. Final settlement is processed within "
                    "forty five days of the last working day.",
                ],
            },
            {
                "heading": "12. Amendment of This Handbook",
                "body": [
                    "The company reserves the right to amend this handbook. Amendments are "
                    "communicated by circular and take effect from the date stated in the "
                    "circular.",
                    "This handbook does not form part of the contract of employment.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D04 - Factory Floor Safety Manual (SCANNED, safety critical)
    # ------------------------------------------------------------------
    "D04": {
        "title": "Factory Floor Safety Manual",
        "sections": [
            {
                "heading": "1. General Safety Rules",
                "body": [
                    "Safety footwear and the issued uniform must be worn at all times on the "
                    "factory floor. No person may enter the production area without "
                    "appropriate personal protective equipment.",
                    "Running is prohibited in all production areas. Walkways marked in yellow "
                    "must be kept clear at all times.",
                    "Smoking is strictly prohibited throughout the premises except in the "
                    "designated area behind the canteen block.",
                ],
            },
            {
                "heading": "2. Personal Protective Equipment",
                "body": [
                    "Ear protection must be worn in the weaving hall and the spinning section "
                    "where noise levels exceed eighty five decibels.",
                    "Eye protection is mandatory during cutting, grinding and any maintenance "
                    "work involving compressed air.",
                    "Dust masks are provided in the blow room and carding section and must be "
                    "worn at all times in those areas.",
                    "Personal protective equipment is issued free of charge. Damaged equipment "
                    "must be reported and replaced before the employee resumes work.",
                ],
            },
            {
                "heading": "3. Machine Safety",
                "body": [
                    "No guard may be removed from any machine while it is in operation. Where "
                    "a guard must be removed for maintenance, the machine must first be "
                    "isolated and locked out.",
                    "Only trained and authorised personnel may operate machinery. A list of "
                    "authorised operators for each machine is displayed at the supervisor's "
                    "desk.",
                    "Loose clothing, jewellery and long unsecured hair are prohibited near "
                    "moving machinery.",
                    "Any unusual noise, vibration, smell or heat from a machine must be "
                    "reported to the supervisor immediately and the machine stopped.",
                ],
            },
            {
                "heading": "4. Lock Out and Tag Out",
                "body": [
                    "Before any maintenance work begins, the energy source must be isolated, "
                    "locked and tagged with the name of the person carrying out the work.",
                    "Only the person who applied a lock may remove it. Removal of another "
                    "person's lock is a serious disciplinary offence.",
                    "The supervisor must verify isolation before work commences and again "
                    "before the machine is returned to service.",
                ],
            },
            {
                "heading": "5. Manual Handling",
                "body": [
                    "Loads exceeding twenty five kilograms must not be lifted by a single "
                    "person. Mechanical aids or assistance from a colleague must be used.",
                    "When lifting, keep the back straight, bend at the knees and hold the "
                    "load close to the body.",
                ],
            },
            {
                "heading": "6. Reporting of Accidents and Near Misses",
                "body": [
                    "All accidents, however minor, must be reported to the supervisor and "
                    "recorded in the accident register within the same shift.",
                    "Near misses must also be reported. A near miss report does not attract "
                    "any penalty and is used only to prevent future accidents.",
                    "The first aid room is located adjacent to the main production hall and "
                    "is staffed during all shifts. The emergency number within the plant is "
                    "extension 100.",
                ],
            },
            {
                "heading": "7. Housekeeping",
                "body": [
                    "Work areas must be left clean at the end of each shift. Waste cotton and "
                    "oily rags must be placed in the designated covered metal bins.",
                    "Spillages of oil or chemicals must be contained and cleaned immediately "
                    "and reported to the supervisor.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D05 - Fire and Evacuation Procedure (SCANNED, safety critical)
    # ------------------------------------------------------------------
    "D05": {
        "title": "Fire and Evacuation Procedure",
        "sections": [
            {
                "heading": "1. On Discovering a Fire",
                "body": [
                    "Raise the alarm immediately by operating the nearest manual call point. "
                    "Call points are located at each stairwell and at both ends of every "
                    "production hall.",
                    "Inform the security office on extension 100. State your name, your "
                    "location and the nature of the fire.",
                    "Attempt to extinguish the fire only if it is small, only if you have "
                    "been trained, and only if you can do so without placing yourself at "
                    "risk. Never attempt to fight a fire that is between you and your exit.",
                ],
            },
            {
                "heading": "2. On Hearing the Alarm",
                "body": [
                    "Stop work immediately. Shut down machinery where it is safe to do so "
                    "using the emergency stop.",
                    "Leave the building by the nearest available exit. Do not stop to collect "
                    "personal belongings.",
                    "Do not use the lifts under any circumstances.",
                    "Close doors behind you as you leave. This slows the spread of fire and "
                    "smoke.",
                ],
            },
            {
                "heading": "3. Assembly Points",
                "body": [
                    "The primary assembly point is the open ground to the north of the "
                    "administrative block, beyond the visitor parking area.",
                    "The secondary assembly point, used when the primary point is unsafe or "
                    "inaccessible, is the loading bay forecourt on the east side.",
                    "Report to your department's fire marshal at the assembly point so that "
                    "a roll call can be taken. Remain at the assembly point until the all "
                    "clear is given by the Chief Fire Marshal.",
                    "Do not re-enter the building for any reason until the all clear has been "
                    "given.",
                ],
            },
            {
                "heading": "4. Fire Marshals",
                "body": [
                    "Each department has at least two nominated fire marshals identifiable by "
                    "yellow high visibility vests. Current names are displayed on the notice "
                    "board in each department.",
                    "Fire marshals sweep their designated area, assist any person requiring "
                    "help to evacuate, and report the outcome of the roll call.",
                ],
            },
            {
                "heading": "5. Fire Extinguisher Types",
                "body": [
                    "Water extinguishers, marked with a red band, are for wood, paper and "
                    "cloth fires only. They must never be used on electrical equipment.",
                    "Carbon dioxide extinguishers, marked with a black band, are for "
                    "electrical fires.",
                    "Dry powder extinguishers, marked with a blue band, may be used on most "
                    "fire types and are located near the chemical store.",
                ],
            },
            {
                "heading": "6. Drills and Training",
                "body": [
                    "Evacuation drills are conducted twice each year. Participation is "
                    "compulsory for all persons on site including visitors and contractors.",
                    "The evacuation target time is four minutes from the sounding of the "
                    "alarm to completion of the roll call.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D06 - Machine Operating Guidelines (SCANNED, Production only)
    # ------------------------------------------------------------------
    "D06": {
        "title": "Machine Operating Guidelines",
        "sections": [
            {
                "heading": "1. Authorisation to Operate",
                "body": [
                    "No person may operate any machine unless they have completed the "
                    "required training and their name appears on the authorised operator "
                    "list for that machine.",
                    "Authorisation is specific to each machine type. Authorisation on one "
                    "machine does not confer authorisation on another.",
                    "Authorisation is reviewed annually and following any incident.",
                ],
            },
            {
                "heading": "2. Pre-Start Checks",
                "body": [
                    "Before starting any machine, confirm that all guards are in place and "
                    "secure, that the emergency stop is accessible and functional, and that "
                    "no tools or materials are left in or on the machine.",
                    "Check lubrication levels and confirm that the previous shift has signed "
                    "the machine log.",
                    "Any defect found during pre-start checks must be reported and the "
                    "machine must not be started until the defect is cleared.",
                ],
            },
            {
                "heading": "3. During Operation",
                "body": [
                    "Never leave a running machine unattended.",
                    "Never reach into a machine to clear a blockage while it is running. "
                    "Stop the machine, isolate it and wait for all movement to cease.",
                    "Report any deviation in output quality, speed or sound to the supervisor "
                    "without delay.",
                ],
            },
            {
                "heading": "4. Shutdown and Handover",
                "body": [
                    "At the end of each shift, stop the machine using the normal stop "
                    "sequence, clean the immediate work area and complete the machine log.",
                    "Record in the log any observation that the incoming operator should be "
                    "aware of, including minor irregularities.",
                ],
            },
            {
                "heading": "5. Breakdown Procedure",
                "body": [
                    "In the event of a breakdown, press the emergency stop, inform the "
                    "supervisor and place the out of service tag on the machine.",
                    "Do not attempt repairs unless you are a member of the maintenance team "
                    "and have completed the lock out and tag out procedure.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D07 - Laptop and IT Asset Policy
    # ------------------------------------------------------------------
    "D07": {
        "title": "Laptop and IT Asset Policy",
        "sections": [
            {
                "heading": "1. Scope",
                "body": [
                    "This policy governs the issue, use, replacement and return of IT assets "
                    "including laptops, desktops, monitors, mobile handsets and data cards.",
                    "It applies to all employees issued with such assets.",
                ],
            },
            {
                "heading": "2. Eligibility",
                "body": [
                    "Laptops are issued to employees in management grades and to employees "
                    "whose role requires mobility, as approved by the department head.",
                    "All other office employees are issued desktop computers.",
                    "Requests for an IT asset are raised through the IT helpdesk with the "
                    "approval of the department head.",
                ],
            },
            {
                "heading": "3. Replacement Cycle",
                "body": [
                    "Laptops are replaced after four years of service or earlier where the "
                    "device is beyond economical repair as assessed by the IT department.",
                    "Desktop computers are replaced after five years of service.",
                    "Mobile handsets, where issued, are replaced after three years.",
                    "Replacement before the end of the standard cycle requires the written "
                    "approval of the Head of Operations.",
                ],
            },
            {
                "heading": "4. Damage and Loss",
                "body": [
                    "Loss or theft of any IT asset must be reported to the IT helpdesk and "
                    "the security office on the same day. Where theft occurs outside company "
                    "premises, a police complaint must be filed and a copy submitted to HR.",
                    "Accidental damage occurring during normal business use is borne by the "
                    "company.",
                    "Where damage or loss results from negligence, the employee may be "
                    "required to bear up to fifty percent of the written down value of the "
                    "asset, subject to a maximum of Rs. 15,000. Negligence is determined by "
                    "the IT department in consultation with HR.",
                ],
            },
            {
                "heading": "5. Software and Data",
                "body": [
                    "Only software approved by the IT department may be installed. Employees "
                    "must not install unlicensed software under any circumstances.",
                    "Company data must be stored in the designated network location or "
                    "approved cloud folder. Storing the sole copy of company data on a local "
                    "drive is not permitted.",
                    "Employees must not connect personal storage devices to company computers "
                    "without IT approval.",
                ],
            },
            {
                "heading": "6. Return of Assets",
                "body": [
                    "All IT assets must be returned to the IT department on or before the last "
                    "working day. Clearance is not issued until all assets are returned.",
                    "The employee must ensure that no personal data remains on the device. The "
                    "IT department wipes all returned devices before reissue.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D08 - IT Support and Escalation Matrix (DOCX, IT only)
    # ------------------------------------------------------------------
    "D08": {
        "title": "IT Support and Escalation Matrix",
        "sections": [
            {
                "heading": "1. Purpose",
                "body": [
                    "This document defines the internal service levels of the IT department "
                    "and the escalation path for unresolved incidents.",
                    "This document is for the internal use of the IT department. It is not "
                    "circulated to other departments.",
                ],
            },
            {
                "heading": "2. Incident Priority Definitions",
                "table": {
                    "caption": "Table 2.1 - Priority definitions and response targets",
                    "columns": ["Priority", "Definition", "Response time", "Resolution target"],
                    "rows": [
                        ["P1", "Production line stopped or full network outage", "15 minutes", "4 hours"],
                        ["P2", "Business function degraded, workaround exists", "1 hour", "1 working day"],
                        ["P3", "Single user unable to work", "4 hours", "2 working days"],
                        ["P4", "Request or minor issue, no work impact", "1 working day", "5 working days"],
                    ],
                },
                "body": [
                    "Priority is assigned by the IT helpdesk on logging and may be revised by "
                    "the IT Manager. The requester may request a review of the assigned "
                    "priority.",
                ],
            },
            {
                "heading": "3. Escalation Path",
                "table": {
                    "caption": "Table 3.1 - Escalation levels",
                    "columns": ["Level", "Owner", "Trigger"],
                    "rows": [
                        ["L1", "IT Helpdesk Executive", "All incidents on logging"],
                        ["L2", "Systems Administrator", "Unresolved at 50% of target"],
                        ["L3", "IT Manager", "Unresolved at 100% of target"],
                        ["L4", "Head of Operations", "P1 unresolved beyond 4 hours"],
                    ],
                },
            },
            {
                "heading": "4. Support Hours",
                "body": [
                    "The IT helpdesk operates from 9:00 am to 6:30 pm Monday to Saturday.",
                    "Outside these hours, P1 incidents only are handled through the on call "
                    "rota. The on call number is published weekly in the IT department.",
                ],
            },
            {
                "heading": "5. Exclusions",
                "body": [
                    "The IT department does not support personally owned devices, personal "
                    "software, or data recovery from devices where company backup procedures "
                    "were not followed.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D09 - Travel and Expense Reimbursement Policy
    # ------------------------------------------------------------------
    "D09": {
        "title": "Travel and Expense Reimbursement Policy",
        "sections": [
            {
                "heading": "1. Scope and Principle",
                "body": [
                    "This policy covers expenses incurred by employees while travelling on "
                    "company business.",
                    "Employees are expected to exercise the same care in incurring expenses "
                    "on company business as they would in managing their own affairs. "
                    "Expenses must be reasonable, necessary and supported by evidence.",
                ],
            },
            {
                "heading": "2. Prior Approval",
                "body": [
                    "All business travel requires prior written approval from the department "
                    "head using Form FIN-12.",
                    "International travel additionally requires the approval of the Managing "
                    "Director.",
                ],
            },
            {
                "heading": "3. Travel Entitlement by Grade",
                "table": {
                    "caption": "Table 3.1 - Mode of travel entitlement",
                    "columns": ["Grade", "Rail", "Air", "Local transport"],
                    "rows": [
                        ["Grade 1 - 2", "Sleeper class", "Not permitted", "Bus or shared auto"],
                        ["Grade 3 - 4", "AC 3 tier", "Not permitted", "Auto rickshaw"],
                        ["Grade 5 - 6", "AC 2 tier", "Economy, over 500 km", "Taxi"],
                        ["Grade 7 and above", "AC 1 tier", "Economy", "Taxi"],
                    ],
                },
            },
            {
                "heading": "4. Daily Allowance",
                "table": {
                    "caption": "Table 4.1 - Daily allowance by grade and city category",
                    "columns": ["Grade", "Metro cities", "Other cities", "Lodging ceiling"],
                    "rows": [
                        ["Grade 1 - 2", "Rs. 600", "Rs. 450", "Rs. 1,500"],
                        ["Grade 3 - 4", "Rs. 900", "Rs. 700", "Rs. 2,500"],
                        ["Grade 5 - 6", "Rs. 1,400", "Rs. 1,100", "Rs. 4,000"],
                        ["Grade 7 and above", "Rs. 2,000", "Rs. 1,600", "Rs. 6,000"],
                    ],
                },
                "body": [
                    "Metro cities for the purpose of this policy are Delhi, Mumbai, Kolkata, "
                    "Chennai, Bengaluru and Hyderabad.",
                    "Daily allowance covers meals and incidental expenses. Separate claims "
                    "for meals are not admissible where daily allowance is claimed.",
                    "Lodging is reimbursed at actuals up to the ceiling shown, against a "
                    "valid GST invoice.",
                ],
            },
            {
                "heading": "5. Claim Submission",
                "body": [
                    "Claims must be submitted within fifteen days of completion of travel "
                    "using Form FIN-14 with original receipts attached.",
                    "Claims submitted after thirty days are not admissible except with the "
                    "written approval of the Head of Operations.",
                    "Reimbursement is processed with the following month's salary.",
                ],
            },
            {
                "heading": "6. Use of Personal Vehicle",
                "body": [
                    "Where a personal vehicle is used with prior approval, mileage is "
                    "reimbursed at Rs. 12 per kilometre for four wheelers and Rs. 5 per "
                    "kilometre for two wheelers.",
                    "Toll and parking charges are reimbursed at actuals against receipts. "
                    "Traffic fines are never reimbursed.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D10 - Salary Grade and Allowance Structure (Finance only)
    # ------------------------------------------------------------------
    "D10": {
        "title": "Salary Grade and Allowance Structure",
        "sections": [
            {
                "heading": "1. Confidentiality",
                "body": [
                    "This document is confidential and restricted to the Finance department "
                    "and authorised members of the management committee.",
                    "It must not be circulated to any other department or to any external "
                    "party. Unauthorised disclosure is a disciplinary offence under the Code "
                    "of Conduct.",
                ],
            },
            {
                "heading": "2. Grade Structure",
                "table": {
                    "caption": "Table 2.1 - Salary grade bands (monthly gross, Rs.)",
                    "columns": ["Grade", "Designation band", "Minimum", "Maximum"],
                    "rows": [
                        ["Grade 1", "Operator, Helper", "14,000", "19,000"],
                        ["Grade 2", "Senior Operator, Assistant", "18,000", "25,000"],
                        ["Grade 3", "Technician, Executive", "24,000", "34,000"],
                        ["Grade 4", "Senior Executive", "32,000", "46,000"],
                        ["Grade 5", "Assistant Manager", "44,000", "62,000"],
                        ["Grade 6", "Manager", "60,000", "88,000"],
                        ["Grade 7", "Senior Manager", "85,000", "1,25,000"],
                        ["Grade 8", "Head of Department", "1,20,000", "1,90,000"],
                    ],
                },
            },
            {
                "heading": "3. Salary Composition",
                "table": {
                    "caption": "Table 3.1 - Standard salary composition",
                    "columns": ["Component", "Basis", "Grades 1 to 4", "Grades 5 and above"],
                    "rows": [
                        ["Basic", "Percentage of gross", "50%", "45%"],
                        ["House rent allowance", "Percentage of basic", "40%", "50%"],
                        ["Conveyance allowance", "Fixed", "Rs. 1,600", "Rs. 3,200"],
                        ["Medical allowance", "Fixed", "Rs. 1,250", "Rs. 2,500"],
                        ["Special allowance", "Balancing figure", "Balance", "Balance"],
                    ],
                },
            },
            {
                "heading": "4. Increment Guidelines",
                "table": {
                    "caption": "Table 4.1 - Increment ranges by performance rating",
                    "columns": ["Rating", "Description", "Increment range"],
                    "rows": [
                        ["A", "Outstanding", "12% - 15%"],
                        ["B", "Exceeds expectations", "8% - 11%"],
                        ["C", "Meets expectations", "5% - 7%"],
                        ["D", "Needs improvement", "0% - 3%"],
                        ["E", "Unsatisfactory", "Nil"],
                    ],
                },
                "body": [
                    "The overall increment budget is approved by the Managing Director each "
                    "February. Individual increments are recommended by department heads "
                    "within the approved budget.",
                ],
            },
            {
                "heading": "5. Promotion Increments",
                "body": [
                    "On promotion to the next grade, a one time increment of eight to twelve "
                    "percent is applied in addition to the annual increment.",
                    "Where the resulting salary falls below the minimum of the new grade, it "
                    "is raised to the grade minimum.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D11 - Provident Fund and Gratuity Guidelines
    # ------------------------------------------------------------------
    "D11": {
        "title": "Provident Fund and Gratuity Guidelines",
        "sections": [
            {
                "heading": "1. Purpose",
                "body": [
                    "This document explains the provident fund and gratuity schemes "
                    "applicable to employees of Nilachala Textiles Pvt. Ltd.",
                    "This document explains the rules of the schemes. It does not contain "
                    "individual account balances. Employees seeking their own provident fund "
                    "balance should use the EPFO member portal or contact the payroll "
                    "executive in the Finance department.",
                ],
            },
            {
                "heading": "2. Provident Fund Contribution",
                "table": {
                    "caption": "Table 2.1 - Provident fund contribution structure",
                    "columns": ["Contribution", "Rate", "Applied to"],
                    "rows": [
                        ["Employee contribution", "12%", "Basic salary"],
                        ["Employer contribution to PF", "3.67%", "Basic salary"],
                        ["Employer contribution to pension", "8.33%", "Basic salary, capped"],
                    ],
                },
                "body": [
                    "Provident fund membership is compulsory for all employees whose basic "
                    "salary is within the statutory ceiling at the time of joining.",
                    "Employees may opt for voluntary provident fund contribution above the "
                    "statutory rate by submitting a request to the payroll executive. The "
                    "employer contribution does not increase correspondingly.",
                ],
            },
            {
                "heading": "3. Provident Fund Withdrawal and Advance",
                "body": [
                    "Partial withdrawal is permitted for specified purposes including "
                    "purchase or construction of a house, medical treatment, marriage and "
                    "higher education, subject to the conditions prescribed by the EPFO.",
                    "Applications are made through the EPFO portal using the Universal "
                    "Account Number. The Finance department attests applications but does not "
                    "control approval or timing, which rest with the EPFO.",
                    "Full withdrawal is permitted only on cessation of employment and after "
                    "the prescribed waiting period.",
                ],
            },
            {
                "heading": "4. Gratuity Eligibility",
                "body": [
                    "Gratuity is payable to employees who have completed five years of "
                    "continuous service, on resignation, retirement or death.",
                    "The five year condition does not apply where employment ceases due to "
                    "death or permanent disablement.",
                ],
            },
            {
                "heading": "5. Gratuity Calculation",
                "body": [
                    "Gratuity is calculated as fifteen days of last drawn basic salary for "
                    "each completed year of service, using a factor of fifteen divided by "
                    "twenty six.",
                    "A period of service exceeding six months in the final year is treated as "
                    "a full year. A period of six months or less is disregarded.",
                    "Gratuity is subject to the statutory maximum in force at the time of "
                    "payment.",
                ],
            },
            {
                "heading": "6. Nomination",
                "body": [
                    "Every employee must file a nomination for provident fund and gratuity "
                    "using Form 2 and Form F respectively within thirty days of joining.",
                    "Nominations should be reviewed following marriage, divorce, birth of a "
                    "child or death of a nominee.",
                ],
            },
        ],
    },

    # ------------------------------------------------------------------
    # D12 - Code of Conduct (DOCX, narrative prose, no tables)
    # ------------------------------------------------------------------
    "D12": {
        "title": "Code of Conduct and Disciplinary Procedure",
        "sections": [
            {
                "heading": "1. Our Standards",
                "body": [
                    "Every employee of Nilachala Textiles Pvt. Ltd. is expected to act with "
                    "honesty, integrity and respect towards colleagues, customers, suppliers "
                    "and the community in which the company operates.",
                    "This code sets out the standards of behaviour expected and the procedure "
                    "followed where those standards are not met. It applies to all employees "
                    "regardless of grade or length of service.",
                ],
            },
            {
                "heading": "2. Conflict of Interest",
                "body": [
                    "Employees must not place themselves in a position where their personal "
                    "interest conflicts, or may be seen to conflict, with the interest of the "
                    "company.",
                    "Any financial or personal interest in a supplier, customer or competitor "
                    "must be declared in writing to the Head of Operations.",
                    "Employees must not accept gifts, hospitality or other benefit from any "
                    "supplier or customer beyond items of nominal value. Any gift received "
                    "must be declared.",
                    "Outside employment or business activity requires prior written approval.",
                ],
            },
            {
                "heading": "3. Confidentiality",
                "body": [
                    "Employees have access to information that is confidential to the company, "
                    "including designs, costings, customer lists, pricing and personnel "
                    "records.",
                    "Such information must not be disclosed to any person outside the company, "
                    "nor to colleagues who do not require it for their work.",
                    "The obligation of confidentiality continues after employment ends.",
                ],
            },
            {
                "heading": "4. Prevention of Harassment",
                "body": [
                    "The company is committed to a workplace free of harassment and "
                    "discrimination on any ground including gender, religion, caste, "
                    "disability or place of origin.",
                    "An Internal Committee is constituted in accordance with the Sexual "
                    "Harassment of Women at Workplace Act. Complaints may be made directly to "
                    "any member of the Internal Committee.",
                    "No employee suffers any detriment for making a complaint in good faith. "
                    "Retaliation against a complainant is itself a serious disciplinary "
                    "offence.",
                ],
            },
            {
                "heading": "5. Misconduct",
                "body": [
                    "Misconduct includes unauthorised absence, insubordination, negligence in "
                    "duty, breach of safety rules, misuse of company property and being under "
                    "the influence of alcohol or drugs on duty.",
                    "Gross misconduct includes theft, fraud, falsification of records, wilful "
                    "damage to property, physical violence, serious breach of safety rules "
                    "endangering others, and disclosure of confidential information.",
                    "Gross misconduct may result in dismissal without notice.",
                ],
            },
            {
                "heading": "6. Disciplinary Procedure",
                "body": [
                    "Where misconduct is alleged, the employee is issued a written charge "
                    "sheet setting out the allegation and is given seven days to respond.",
                    "Where the response is not accepted, a domestic enquiry is conducted by an "
                    "enquiry officer who is not connected with the matter. The employee may be "
                    "accompanied by a colleague of their choice.",
                    "The employee is given the opportunity to examine documents relied upon, "
                    "to question witnesses and to present their own evidence.",
                    "The enquiry officer submits findings to the Head of Operations, who "
                    "decides the outcome. The decision is communicated in writing with "
                    "reasons.",
                ],
            },
            {
                "heading": "7. Disciplinary Outcomes",
                "body": [
                    "Outcomes range from a verbal warning, a written warning, withholding of "
                    "increment, demotion, suspension without pay, to dismissal, according to "
                    "the gravity of the misconduct and any previous record.",
                    "A written warning remains on the employee's record for twelve months and "
                    "is disregarded thereafter provided there is no repetition.",
                ],
            },
            {
                "heading": "8. Appeal",
                "body": [
                    "An employee may appeal against any disciplinary outcome by writing to the "
                    "Managing Director within fourteen days of receiving the decision.",
                    "The appeal decision is final within the company.",
                ],
            },
        ],
    },
}
