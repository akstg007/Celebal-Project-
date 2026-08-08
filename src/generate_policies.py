"""
Day 2 - Generate synthetic hospital policy documents.

These are entirely fictional, written for this project (no real hospital's
actual policies) — the "synthetically generated hospital policy documents"
the project brief asks for. They become the knowledge base for the RAG Agent.

Run:
    python src/generate_policies.py
"""

from pathlib import Path

OUT_DIR = Path(__file__).parent.parent / "data" / "policies"

POLICIES = {

"admission_policy.txt": """HOSPITAL POLICY: PATIENT ADMISSION PROCEDURE
Document ID: POL-ADM-01 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
This policy defines the standard procedure for admitting patients across all
hospital departments, ensuring consistent, safe, and timely intake regardless
of admission type (Elective, Urgent, or Emergency).

2. SCOPE
Applies to all clinical and administrative staff involved in patient intake,
including front-desk registration, triage nurses, and admitting physicians.

3. ADMISSION TYPES
- Elective Admission: Scheduled in advance, typically for planned procedures.
  Requires pre-admission clearance, insurance pre-authorization, and a signed
  consent form at least 48 hours prior to the scheduled date.
- Urgent Admission: Patient requires care within 24 hours but is not in
  immediate life-threatening danger. Triage nurse assigns priority level
  within 30 minutes of arrival.
- Emergency Admission: Immediate, life-threatening condition. Patient is
  admitted directly to the Emergency Department without prior registration;
  paperwork is completed retroactively within 24 hours or upon stabilization.

4. PROCEDURE
4.1. Registration staff verify patient identity using two identifiers (full
name and date of birth) and collect insurance information.
4.2. A unique patient ID is generated and a wristband issued before any
clinical procedure is performed.
4.3. Triage nurse records vital signs and assigns an admission type within
15 minutes of registration for Urgent cases, immediately for Emergency cases.
4.4. Attending physician is notified and reviews the patient's history within
1 hour of ward admission.
4.5. Room and bed assignment is made based on medical condition, required
level of care, and current bed availability, per the Room Allocation Policy.

5. DOCUMENTATION
All admissions must be logged in the hospital information system within 2
hours, including admission type, attending doctor, and assigned room number.

6. EXCEPTIONS
Mass-casualty events invoke the Emergency Surge Protocol, which supersedes
standard registration timelines (see Emergency Protocols document).
""",

"discharge_policy.txt": """HOSPITAL POLICY: PATIENT DISCHARGE PROCEDURE
Document ID: POL-DIS-02 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To ensure every patient is discharged safely, with complete documentation,
clear follow-up instructions, and appropriate handoff of care.

2. DISCHARGE CRITERIA
A patient may be discharged when the attending physician determines that:
- Vital signs are stable for at least 12 consecutive hours.
- The primary reason for admission has been resolved or is manageable on an
  outpatient basis.
- A safe discharge destination (home, rehabilitation facility, or transfer)
  has been confirmed.

3. DISCHARGE PROCEDURE
3.1. Attending physician writes a discharge order in the patient's chart,
including diagnosis summary, procedures performed, and medications.
3.2. Nursing staff review discharge instructions with the patient or their
designated caregiver, covering medication schedule, activity restrictions,
warning signs requiring return to hospital, and follow-up appointment dates.
3.3. Billing department finalizes the patient's account; any outstanding
balance is communicated in writing per the Billing & Insurance Policy.
3.4. A discharge summary is sent to the patient's primary care physician
within 48 hours, where applicable.
3.5. Patient or caregiver signs an acknowledgment of receiving discharge
instructions before leaving the ward.

4. AGAINST MEDICAL ADVICE (AMA) DISCHARGE
If a patient chooses to leave against medical advice, the attending
physician must document the risks explained to the patient, and the patient
must sign an AMA release form. Care is not withheld pending this signature
if delay would endanger the patient.

5. READMISSION
Patients readmitted within 30 days for the same condition trigger an
internal quality review to assess whether the original discharge was
premature.
""",

"billing_insurance_policy.txt": """HOSPITAL POLICY: BILLING AND INSURANCE PROCEDURE
Document ID: POL-BIL-03 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To ensure transparent, accurate, and timely billing for all services
rendered, and to define how the hospital coordinates with insurance
providers.

2. ACCEPTED INSURANCE PROVIDERS
The hospital directly bills the following providers: Blue Cross, Medicare,
Aetna, UnitedHealthcare, and Cigna. Patients with other providers may submit
claims for reimbursement themselves using an itemized invoice.

3. PRE-AUTHORIZATION
For Elective admissions, insurance pre-authorization must be obtained by the
billing department at least 48 hours before the scheduled procedure. Urgent
and Emergency admissions are billed retroactively; pre-authorization is not
required to deliver care.

4. BILLING PROCEDURE
4.1. An itemized bill is generated at discharge, covering room charges,
procedures, medication, and physician fees.
4.2. The billing department submits claims to the patient's insurance
provider within 5 business days of discharge.
4.3. Patients receive a summary of any co-payment or deductible owed within
10 business days of discharge.
4.4. Disputed charges must be raised in writing within 30 days of the bill
date and are reviewed by the billing manager within 10 business days.

5. FINANCIAL ASSISTANCE
Patients facing financial hardship may apply for a payment plan or a
reduction in billed amount through the Patient Financial Services office.
Applications are reviewed within 15 business days.

6. REFUNDS
Overpayments identified during reconciliation are refunded to the patient
or insurance provider within 30 days of discovery, per the Refund and
Cancellation Policy.
""",

"visiting_hours_policy.txt": """HOSPITAL POLICY: VISITOR ACCESS AND VISITING HOURS
Document ID: POL-VIS-04 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To balance patient rest and privacy with the well-documented benefits of
family and social support during a hospital stay.

2. STANDARD VISITING HOURS
General wards: 10:00 AM - 8:00 PM daily.
Intensive Care Unit (ICU): 11:00 AM - 1:00 PM and 5:00 PM - 7:00 PM, limited
to two visitors at a time.
Maternity ward: 10:00 AM - 8:00 PM, immediate family only for the first 24
hours post-delivery.

3. VISITOR LIMITS
A maximum of two visitors per patient at any time in general wards, unless
otherwise approved by the charge nurse for end-of-life or special
circumstances.

4. EXCEPTIONS AND RESTRICTIONS
4.1. Attending physicians may restrict visitation for patients under
infection control precautions (see Infection Control Policy), immediately
post-surgery, or when the patient's condition requires it.
4.2. Children under 12 must be accompanied by an adult and are not permitted
in the ICU except for immediate family in critical situations.
4.3. Visitors displaying symptoms of contagious illness will be asked to
reschedule their visit.

5. AFTER-HOURS VISITATION
Exceptions to standard hours may be granted by the charge nurse for
out-of-town family, end-of-life situations, or patients under 18. All
after-hours visitors must check in at the main security desk.
""",

"infection_control_policy.txt": """HOSPITAL POLICY: INFECTION PREVENTION AND CONTROL
Document ID: POL-INF-05 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To minimize the risk of healthcare-associated infections (HAIs) for
patients, staff, and visitors.

2. STANDARD PRECAUTIONS
All staff must perform hand hygiene before and after every patient contact,
using alcohol-based hand rub or soap and water for a minimum of 20 seconds.
Personal protective equipment (PPE) — gloves, gowns, masks — is required
based on the anticipated exposure risk for each procedure.

3. ISOLATION PRECAUTIONS
Patients with confirmed or suspected communicable infections are placed
under one of three isolation categories:
- Contact Precautions: gloves and gown required for all room entry.
- Droplet Precautions: surgical mask required within 3 feet of the patient.
- Airborne Precautions: N95 respirator required; patient placed in a
  negative-pressure room where available.

4. ENVIRONMENTAL CLEANING
Patient rooms are terminally cleaned and disinfected within 2 hours of
discharge, before the next patient is assigned. High-touch surfaces (bed
rails, call buttons, door handles) are disinfected at minimum every 8 hours
during a patient's stay.

5. STAFF ILLNESS
Staff exhibiting symptoms of a communicable illness must not report to
direct patient care duties and must notify their supervisor and Occupational
Health before returning to work.

6. OUTBREAK RESPONSE
Two or more cases of the same infection in the same ward within 72 hours
triggers activation of the Infection Control Committee and mandatory
enhanced surveillance of that ward.
""",

"data_privacy_policy.txt": """HOSPITAL POLICY: PATIENT DATA PRIVACY AND CONFIDENTIALITY
Document ID: POL-PRIV-06 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To protect the confidentiality, integrity, and appropriate use of patient
health information in accordance with hospital data governance standards.

2. ACCESS CONTROL
Access to patient records is granted strictly on a need-to-know basis tied
to a staff member's role. All access to the electronic health record system
is logged, including staff ID, timestamp, and record accessed.

3. PERMITTED USES
Patient information may be accessed and shared for: direct treatment
purposes, care coordination with other treating providers, billing and
insurance claims processing, and legally mandated public health reporting.

4. DISCLOSURE TO THIRD PARTIES
Patient information is not disclosed to family members, employers, or any
external party without the patient's written consent, except where required
by law (e.g., certain communicable disease reporting) or in
life-threatening emergencies where the patient cannot consent.

5. DATA SECURITY
All patient data is encrypted at rest and in transit. Staff must not access
patient records for any patient they are not directly involved in treating,
including friends, family members, or public figures ("curiosity access"),
which is treated as a serious disciplinary violation.

6. PATIENT RIGHTS
Patients may request a copy of their medical record, request corrections to
inaccurate information, and request a log of who has accessed their record,
processed by the Health Information Management office within 15 business
days.

7. BREACH NOTIFICATION
Any suspected unauthorized access or data breach must be reported to the
Privacy Officer within 4 hours of discovery.
""",

"emergency_protocols.txt": """HOSPITAL POLICY: EMERGENCY RESPONSE PROTOCOLS
Document ID: POL-EMR-07 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To provide a coordinated, rapid response to medical emergencies, mass
casualty events, and internal hospital emergencies (fire, power failure,
security threats).

2. CODE SYSTEM
- Code Blue: Adult cardiac or respiratory arrest. Response team must reach
  the patient within 3 minutes of the call.
- Code Red: Fire. Nearest staff activate the nearest fire alarm and begin
  the RACE protocol (Rescue, Alarm, Contain, Extinguish/Evacuate).
- Code Silver: Active security threat or weapon on premises. Ward is
  immediately locked down; only Security and law enforcement may unlock.
- Code Pink: Infant or child abduction. All exits are monitored and a
  facility-wide lockdown is initiated within 2 minutes.

3. MASS CASUALTY / SURGE PROTOCOL
Activated when incoming patients exceed normal Emergency Department
capacity by 50% or more. Elective admissions are paused, additional staff
are called in per the on-call roster, and triage follows the START (Simple
Triage and Rapid Treatment) method to prioritize care.

4. EVACUATION
In the event of full facility evacuation, patients are moved in order of
mobility: ambulatory patients first (to preserve staff capacity for
non-ambulatory patients), followed by wheelchair-assisted, then bedbound
patients requiring full transport teams.

5. COMMUNICATION
The hospital Incident Commander is responsible for all external
communication during a declared emergency; individual staff must direct
media or public inquiries to the Incident Commander's office.
""",

"medication_administration_policy.txt": """HOSPITAL POLICY: MEDICATION ADMINISTRATION
Document ID: POL-MED-08 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To ensure medications are prescribed, dispensed, and administered safely
and accurately.

2. THE FIVE RIGHTS
Before administering any medication, nursing staff must verify: the right
patient, right medication, right dose, right route, and right time, cross-
checked against the physician's order and the patient's wristband.

3. HIGH-ALERT MEDICATIONS
Medications with a heightened risk of causing significant harm if
administered incorrectly (e.g., insulin, anticoagulants, opioids) require an
independent double-check by a second licensed nurse before administration.

4. DOCUMENTATION
Every administered dose is recorded in the electronic medication
administration record (eMAR) immediately after administration, including
time, dose, and administering nurse's ID. Missed or refused doses are also
documented, with reason.

5. ADVERSE REACTIONS
Any suspected adverse drug reaction must be reported immediately to the
attending physician and logged in the incident reporting system within 1
hour. Severe reactions trigger an automatic pharmacy and safety review.

6. MEDICATION RECONCILIATION
On admission and at discharge, a full medication reconciliation is performed
comparing home medications, current inpatient medications, and
newly-prescribed discharge medications to prevent duplication or dangerous
interactions.
""",

"room_allocation_policy.txt": """HOSPITAL POLICY: ROOM AND BED ALLOCATION
Document ID: POL-ROOM-09 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To allocate rooms and beds fairly and appropriately based on clinical need,
infection control requirements, and patient acuity.

2. ALLOCATION PRIORITY
Bed assignment priority is determined by: (1) clinical acuity and required
level of monitoring, (2) infection control isolation requirements, (3)
specialty ward matching the patient's primary condition, and (4) patient
preference where clinically equivalent options exist.

3. WARD ASSIGNMENT BY CONDITION
Patients are generally assigned to the ward most aligned with their primary
medical condition (e.g., Oncology for Cancer patients, Cardiology for
Hypertension-related admissions) where capacity allows, to ensure access to
specialty nursing expertise.

4. PRIVATE ROOM REQUESTS
Private rooms are allocated based on medical necessity first (e.g.,
isolation precautions) and subject to availability for patient preference
requests, which may incur an additional charge as outlined in the Billing
Policy.

5. ROOM TRANSFERS
A patient may be transferred between rooms or wards if their clinical
condition changes significantly, if isolation status changes, or for
operational reasons (e.g., consolidating a ward for maintenance). Transfers
are documented with reason and approving physician.

6. CAPACITY MANAGEMENT
When the hospital is at full capacity, the bed management team coordinates
with Admissions to determine whether new Elective admissions should be
deferred, following the Admission Policy's exception procedures.
""",

"complaint_grievance_policy.txt": """HOSPITAL POLICY: PATIENT COMPLAINT AND GRIEVANCE PROCEDURE
Document ID: POL-COMP-10 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To provide patients and families a clear, fair process to raise concerns
about their care or experience, and to ensure concerns are addressed
promptly.

2. HOW TO FILE A COMPLAINT
Complaints may be raised verbally with any staff member, the charge nurse,
or Patient Relations, or submitted in writing via the Patient Relations
office. Verbal complaints that cannot be resolved on the spot are escalated
to Patient Relations within 24 hours.

3. RESPONSE TIMELINE
- Acknowledgment of a written complaint: within 2 business days.
- Investigation and initial response: within 7 business days for standard
  complaints, or within 30 days for complex complaints requiring a clinical
  review.
4. GRIEVANCE ESCALATION
If a patient is not satisfied with the initial response, they may formally
escalate to a grievance, which is reviewed by the Patient Relations
Director and, where clinical care is in question, a physician not involved
in the original care.

5. NON-RETALIATION
Filing a complaint or grievance will never affect the quality of care a
patient receives. Staff are prohibited from retaliating against a patient
or family member for raising a concern.

6. EXTERNAL ESCALATION
Patients who remain unsatisfied after the internal grievance process may
escalate to the relevant state health department or accreditation body;
contact information is provided in the official grievance response letter.
""",

"patient_rights_policy.txt": """HOSPITAL POLICY: PATIENT RIGHTS AND RESPONSIBILITIES
Document ID: POL-RIGHT-11 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PATIENT RIGHTS
Every patient has the right to: receive respectful and non-discriminatory
care; be informed about their diagnosis, treatment options, and prognosis in
understandable language; participate in decisions about their care,
including the right to refuse treatment; receive care in a safe environment
free from abuse or harassment; access their own medical records; and have
their pain assessed and managed appropriately.

2. INFORMED CONSENT
Before any procedure carrying material risk, the treating physician must
explain the procedure, its risks, benefits, and alternatives, and obtain the
patient's (or authorized representative's) written consent, except in
emergencies where delay would endanger life.

3. PATIENT RESPONSIBILITIES
Patients are asked to: provide accurate information about their health
history, ask questions if instructions are unclear, follow the agreed
treatment plan or discuss concerns with their care team, and treat staff and
other patients with respect.

4. ADVANCE DIRECTIVES
Patients have the right to establish an advance directive (living will or
healthcare power of attorney) and to have it honored by the care team,
consistent with applicable law.

5. NON-DISCRIMINATION
Care is provided without discrimination on the basis of race, religion,
gender, sexual orientation, disability, national origin, or ability to pay,
consistent with the hospital's Non-Discrimination Policy.
""",

"fire_safety_policy.txt": """HOSPITAL POLICY: FIRE SAFETY AND EVACUATION
Document ID: POL-FIRE-12 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To protect patients, staff, and visitors in the event of a fire, and to
ensure staff know their role in fire response.

2. RACE PROTOCOL
All staff are trained in the RACE protocol upon hire and annually:
- Rescue anyone in immediate danger.
- Alarm: activate the nearest fire alarm pull station and notify the
  switchboard, which pages a facility-wide "Code Red" with location.
- Contain: close all doors to slow fire and smoke spread.
- Extinguish (small, contained fires only, using a PASS-technique fire
  extinguisher) or Evacuate if the fire cannot be safely contained.

3. HORIZONTAL EVACUATION
The primary evacuation strategy for patient care areas is horizontal —
moving patients through fire doors to an adjacent, unaffected smoke
compartment on the same floor — since patients are often non-ambulatory.
Vertical evacuation (moving between floors) is only used if the current
compartment becomes untenable.

4. FIRE DRILLS
Fire drills are conducted quarterly on each shift. All staff must
participate and drills are logged, including response time and any
identified gaps.

5. EQUIPMENT MAINTENANCE
Fire extinguishers, alarm pull stations, and sprinkler systems are inspected
monthly by Facilities and tested annually by a certified fire safety
contractor.
""",

"consent_for_treatment_policy.txt": """HOSPITAL POLICY: CONSENT FOR TREATMENT
Document ID: POL-CONS-13 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To ensure patients provide informed, voluntary consent before undergoing
treatment, consistent with their right to self-determination.

2. TYPES OF CONSENT
- General Consent: obtained at admission, covering routine care such as
  vital sign monitoring, basic nursing care, and diagnostic blood draws.
- Informed Consent: required for any procedure with material risk (surgery,
  anesthesia, invasive diagnostic procedures, blood transfusion), obtained
  by the physician performing or supervising the procedure.

3. CAPACITY TO CONSENT
Adult patients are presumed to have capacity to consent unless a physician
documents otherwise. Where a patient lacks capacity, consent is obtained
from their legally authorized representative in the following priority
order: healthcare power of attorney, legal guardian, spouse, adult child,
parent, then closest available adult relative.

4. MINORS
Consent for patients under 18 is generally obtained from a parent or legal
guardian, except for specific categories defined by law (e.g., emergency
care, certain reproductive or mental health services) where a minor may
consent independently.

5. WITHDRAWAL OF CONSENT
A patient may withdraw consent at any point before or during a procedure,
except where stopping would itself create immediate danger to the patient's
life.

6. EMERGENCY EXCEPTION
Where a patient requires immediate treatment to prevent death or serious
harm and is unable to consent, and no authorized representative is
immediately available, treatment may proceed under the emergency exception,
documented in detail in the chart.
""",

"non_discrimination_policy.txt": """HOSPITAL POLICY: NON-DISCRIMINATION AND EQUAL ACCESS
Document ID: POL-NONDIS-14 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To affirm the hospital's commitment to providing equitable access to care
for every patient.

2. POLICY STATEMENT
The hospital does not discriminate in the provision of care, admission,
room assignment, or any other service on the basis of race, color,
national origin, religion, sex, gender identity, sexual orientation, age,
disability, or ability to pay.

3. LANGUAGE ACCESS
Qualified medical interpreters (in-person or via telephonic/video service)
are provided free of charge to any patient with limited English
proficiency. Family members, especially minors, must not be used as
interpreters for clinical discussions except in genuine emergencies where
no interpreter is available.

4. ACCESSIBILITY
The hospital provides reasonable accommodation for patients with
disabilities, including accessible rooms, communication aids for patients
who are deaf or hard of hearing, and equipment such as accessible exam
tables where clinically required.

5. REPORTING DISCRIMINATION
Any patient, family member, or staff member who believes discrimination has
occurred may report it to Patient Relations or Human Resources without fear
of retaliation, per the Complaint and Grievance Policy.
""",

"refund_cancellation_policy.txt": """HOSPITAL POLICY: REFUNDS AND APPOINTMENT CANCELLATION
Document ID: POL-REF-15 | Effective Date: 2024-01-01 | Review Cycle: Annual

1. PURPOSE
To set clear expectations for cancelling scheduled (Elective) admissions or
procedures, and for processing billing refunds.

2. CANCELLATION OF ELECTIVE ADMISSIONS
Patients may cancel or reschedule a scheduled Elective admission free of
charge with at least 24 hours' notice. Cancellations with less than 24
hours' notice may incur a rescheduling fee, waived in cases of documented
medical emergency.

3. HOSPITAL-INITIATED CANCELLATION
If the hospital must cancel or postpone a scheduled procedure (e.g., due to
emergency bed capacity needs), the patient is notified as early as possible
and rescheduled at the earliest available slot with priority status.

4. REFUND PROCESSING
Refunds due to overpayment, billing error, or cancelled procedures are
processed within 30 days of the refund being approved, returned via the
original payment method where possible.

5. DISPUTED CHARGES
Refund requests tied to a disputed charge follow the timeline in the
Billing and Insurance Policy; refunds are only issued after the dispute
review is complete.
""",

}


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for filename, content in POLICIES.items():
        (OUT_DIR / filename).write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Wrote {len(POLICIES)} policy documents to {OUT_DIR}")


if __name__ == "__main__":
    main()
