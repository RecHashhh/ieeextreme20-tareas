# IEEE Global Expert Selection Challenge

**Tipo:** Estándar · **Límite de tiempo:** 4000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

## IEEE Xplore

Warm greetings to all IEEExtreme Participants from the Xplore API Team! 

As part of the IEEExtreme Competition, you will face a programming challenge where you'll need to analyze web application logs to identify potential instances of application misuse.

For a full dynamic database search IEEE Xplore API is available for your IEEE research needs. Xplore API provides metadata on 4.9mm academic works and is now delivering full-text content on 50k 'Open Access' articles. Xplore API will make your research needs fast and easy. The Xplore API Portal supports PHP, Python and Java as well as providing output in JSON and XML formats. Many API use cases are listed within the API Portal. 

Xplore API registration is free. To learn more about IEEE Xplore API please visit [developer.ieee.org/](https://developer.ieee.org/) and register for an API key TODAY! 

## Challenge

The IEEE Technical Activities Board is establishing several specialized Working Groups (WGs) to draft next generation technical standards. To ensure optimal international collaboration, efficiency, and depth of knowledge, the selection of committee members must be strictly quantified and automated. You are tasked with building a tool that parses a standardized registry file of domain experts and programmatically selects a defined number of individuals (X) to form an elite working committee based on dynamic, challenge-specific constraints and optimization metrics. 

## Standard input

All entry data is loaded dynamically from a flat comma-separated file. The file contains a header row followed by multiple expert records. Each record consists of the following six fields in no specific order:

1. Expert Id
2. Name
3. Domains 
4. Education
5. Years of Experience
6. Time Zone

The first line of the file will be the selection criteria and the “Expert Id” of the committee chair.  The second line will be the header for each of the metadata fields above.  The following lines will be the expert information.

## Standard output

The sorting will be based on a primary sort of “Education”, based on the level achieved.  The orders are 1) PhD, 2) Masters, 3) Undergraduate, 4) Associates. “Years of Experience” in descending order, and lastly “Expert Id” in ascending order.   List the records in the same format as the input data.

## Constraints and notes

- $\text{Records} \leq 10,000$.
- “Education” will be limited to PhD, Masters, Undergraduate, Associates.  PhD being the highest level of achievement and Associates the lowest.
- “Time Zone” will be an integer in the range $[-12, 14]$.
- “Years of Experience” will be an integer in the range $[0, 60]$.
- The “Selection Criteria” will take the format: “Committee Chair Id”, “Experts Needed”, “Education Level”, “Years of Experience”, “Domain”, “Time Zone Difference”.  There will always be one domain in the selection criteria.
- If the number of experts that fit the criteria is greater than needed the precedence will be “Education”, “Years of Experience”, and finally “Time Zone” proximity to chair.  There will never be a case where there will be a tie for all three of these data points.

### Ejemplo 1

Entrada:

```
EXP_0005, 2, Undergraduate, 5, Electromagnetism, 2
Expert Id, Name, Domains, Education, Years of Experience, Time Zone
EXP_0001, Hans Mueller, Electromagnetism; Physics; Quantum Mechanics;, Masters, 10, -02:00
EXP_0002, Oliver Benoit, Materials; Lasers;, PhD, 9, -02:00
EXP_0003, Priya Sharma, Electromagnetism; Physics; Hysteresis;, Masters, 12, -05:00
EXP_0004, Elena Rostova, Electromagnetism; Mathematics;, Masters, 15, -02:00
EXP_0005, David Miller, Computer Programming; Electromagnetism; Image transformation;, Masters, 5, +00:00
EXP_0006, Lin Wei, Electromagnetism;, PhD, 8, -01:00
```

Salida:

```
EXP_0005, David Miller, Computer Programming; Electromagnetism; Image transformation;, Masters, 5, +00:00
EXP_0006, Lin Wei, Electromagnetism;, PhD, 8, -01:00
EXP_0004, Elena Rostova, Electromagnetism; Mathematics;, Masters, 15, -02:00
```

Explicación:

`EXP_0005` is the committee chair and shows up first in the output.  Eliminate expert `EXP_0002` because the domain does not match the criteria.  Eliminate expert `EXP_0003` because the `Time Zone` doesn’t match the criteria.  Expert `EXP_0006` is the only expert that fits the criteria and has a `PhD`.  The following experts meet the criteria, `EXP_0001`, `EXP_0004` and have `Masters` degrees. `EXP_0004` is chosen because of `Years of Experience`.
