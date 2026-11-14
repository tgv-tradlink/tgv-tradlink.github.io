"""Buyer-facing detail for each product: key features, installation steps and buying tips.
Installation steps follow common manufacturer practice; always follow site drawings and
applicable codes for spacing and loads."""

C = {}

C['split'] = dict(
    features=[
        ('Vibration damping', 'EPDM lining absorbs pump and flow vibration and cuts noise carried into the building.'),
        ('Protects the pipe', 'Rubber keeps metal off the pipe surface — no scratches, no coating damage, no metal-to-metal contact.'),
        ('Fits installed pipe', 'Two-piece design opens fully, so the clamp goes around a pipe that is already in place.'),
        ('Hot & cold lines', 'EPDM performs on both hot and cold water services.'),
        ('Rod or wall mounting', 'Threaded boss takes a drop rod from the ceiling or a bolt into a wall or channel.'),
    ],
    install=[
        ('Mark support points', 'Mark clamp positions along the pipe run as per the drawing or site practice.'),
        ('Fix the rod', 'Fix a bullet anchor in the slab and screw in the threaded rod (or bolt to a channel / wall).'),
        ('Mount the clamp', 'Screw the clamp boss onto the rod and set the height.'),
        ('Close around the pipe', 'Open the clamp, rest the pipe in the lower half, close the top half.'),
        ('Tighten evenly', 'Tighten both screws in turns until the rubber grips — snug, not crushed. Lock the rod with a nut.'),
    ],
    tips=[
        'Order by pipe size — a 2″ clamp fits 2″ NB pipe. For PPR / CPVC, check the outside diameter on the size reference page.',
        'Rubber-lined clamps are the right choice on copper, stainless steel and plastic pipes.',
        'Pair with BA series bullet anchors and threaded rod for ceiling hanging, or CH / CL series for channel mounting.',
    ])

C['ubolt'] = dict(
    features=[
        ('Ready to fix', 'Supplied with washers and nuts on both legs — no extra hardware to source.'),
        ('Cushioned grip', 'Ribbed EPDM sleeve holds the pipe firmly while protecting its surface.'),
        ('Quieter lines', 'Rubber breaks the metal path, reducing vibration and water-hammer noise.'),
        ('Strong 8 mm rod', 'Formed from 8 mm rod with threaded ends for a secure, adjustable hold.'),
        ('Mounts anywhere', 'Works on slotted channel, angle iron, cantilever arms and wall brackets.'),
    ],
    install=[
        ('Prepare the support', 'Fix the channel, angle or bracket in line with the pipe run.'),
        ('Drill or use slots', 'Drill two holes at the U-bolt leg spacing, or use the slots of a slotted channel.'),
        ('Place the pipe', 'Rest the pipe on the support where the clamp will go.'),
        ('Fit the U-bolt', 'Pass the U-bolt over the pipe and both legs through the holes.'),
        ('Tighten alternately', 'Fit washers and nuts, tighten left and right in turns until the rubber is snug.'),
    ],
    tips=[
        'Order by pipe size — leg spacing is made to match each nominal size.',
        'For long horizontal runs, combine with CL cantilevers or CH channel for a neat, level line.',
        'Do not over-tighten on plastic pipe — the rubber should compress lightly, not flatten.',
    ])

C['leaf'] = dict(
    features=[
        ('Wide 32 mm strip', 'Spreads the load over a wider band — ideal for larger and heavier pipes.'),
        ('Channel-ready feet', 'Notched feet lock into the lips of 41 × 41 slotted channel for a positive hold.'),
        ('Bolted closure', 'A single bolt and nut through the top ears clamps the pipe tight.'),
        ('Heavier gauge on big sizes', '1.5 mm strip up to 3″; 2 mm strip from 4″ to 12″.'),
        ('Up to 12″', '13 sizes cover branch lines through to mains and risers.'),
    ],
    install=[
        ('Fix the channel', 'Mount slotted channel (CH) or a cantilever arm (CL) at the support point.'),
        ('Seat the pipe', 'Rest the pipe on the channel face.'),
        ('Fit both halves', 'Place the two leaves around the pipe with the feet engaged in the channel lips.'),
        ('Insert the bolt', 'Pass the bolt through the top ears and fit the nut.'),
        ('Tighten', 'Tighten until the clamp holds the pipe firmly against the channel.'),
    ],
    tips=[
        'Designed to work with our 41 × 41 slotted channel (CH-801) and cantilevers (CL series).',
        'For vibration-prone lines, consider rubber-lined split clamps (SC series) on smaller sizes.',
        'Length per size is listed with each item code — useful for checking clearance.',
    ])

C['sprinkler'] = dict(
    features=[
        ('Made for fire lines', 'Band hanger profile widely used on sprinkler and fire-hydrant mains and branches.'),
        ('Height adjustable', 'Hangs from a threaded drop rod — adjust the nut to set level and slope.'),
        ('Fast to install', 'Slip the pipe into the loop; no clamping screws to tighten around the pipe.'),
        ('Two gauges', '2 mm (14G) for heavier runs, 1.5 mm (16G) for lighter lines.'),
        ('1″ to 8″', 'Nine sizes from branch lines to mains.'),
    ],
    install=[
        ('Anchor the ceiling', 'Drill and set a bullet anchor (BA series) in the slab at each hanger point.'),
        ('Fit the drop rod', 'Screw threaded rod into the anchor and cut to the required drop.'),
        ('Hang the band', 'Pass the rod through the hanger top hole; fit nuts above and below.'),
        ('Load the pipe', 'Slip the pipe into the hanger loops along the run.'),
        ('Level & lock', 'Adjust the nuts to set height and slope, then lock tight.'),
    ],
    tips=[
        'Pick 14G for larger diameters and long spans; 16G suits lighter branch lines.',
        'Follow your fire-protection drawings and local code for hanger spacing.',
        'Order bullet anchors (BA series) and threaded rod together for a complete hanging set.',
    ])

C['gi'] = dict(
    features=[
        ('Clean, low-profile fixing', 'Saddle holds the pipe flat against a wall or ceiling.'),
        ('Galvanised for protection', 'G.I. finish resists rust in normal indoor and service areas.'),
        ('Stainless option', 'S.S. clamps for wet, coastal, chemical or exposed locations.'),
        ('Two G.I. thicknesses', '1.2 mm for light lines, 1.5 mm for heavier pipes.'),
        ('Economical', 'The quickest and most cost-effective way to fix surface-run pipes.'),
    ],
    install=[
        ('Position the pipe', 'Hold the pipe in its final position against the surface.'),
        ('Mark the holes', 'Place the saddle over the pipe and mark both fixing holes.'),
        ('Drill & plug', 'Drill the holes and insert wall plugs or suitable anchors.'),
        ('Screw down', 'Fix the saddle with screws, tightening both sides evenly.'),
    ],
    tips=[
        'Choose S.S. 1.0 mm for bathrooms, terraces, coastal sites and chemical areas.',
        'Order by pipe size from ½″ to 6″ (15 – 150 mm).',
        'Also suits electrical conduit and gas lines run along walls.',
    ])

C['cantilever'] = dict(
    features=[
        ('Ready-welded', 'Arm comes welded to its base plate — just anchor it and load it.'),
        ('Slotted arm', 'Takes channel nuts, leaf clamps, U-bolts and brackets at any point along its length.'),
        ('Seven lengths', '150 mm to 750 mm, from single pipes to multi-service runs.'),
        ('41 × 41 profile', 'Fully compatible with our slotted channel and base plates.'),
        ('Wall or column', 'Fixes to concrete walls, columns and steel members.'),
    ],
    install=[
        ('Mark the position', 'Mark the base plate holes on the wall, level with the pipe run.'),
        ('Drill & anchor', 'Drill and fix wedge anchors (WA series) through the base plate holes.'),
        ('Tighten anchors', 'Tighten anchor nuts to fix the arm firmly and level.'),
        ('Fit the clamps', 'Fix pipe clamps (LC / UB series) to the arm using the slots.'),
        ('Load & check', 'Place the pipes, tighten the clamps and check the arm is level.'),
    ],
    tips=[
        'Choose the arm length to cover the pipe(s) plus clearance from the wall.',
        'Use wedge anchors (WA series) in solid concrete for a permanent fixing.',
        'Space cantilevers as per the pipe size and load shown in your drawings.',
    ])

C['baseplate'] = dict(
    features=[
        ('Heavy 4 mm plate', '150 × 150 mm plate spreads load into the slab.'),
        ('Channel socket', 'Takes 41 × 41 slotted channel to build posts and frames.'),
        ('Floor or ceiling', 'Use it to stand supports up from the floor or drop them from the slab.'),
    ],
    install=[
        ('Mark & drill', 'Mark the plate holes and drill for anchors.'),
        ('Anchor the plate', 'Fix with wedge anchors (WA series) and tighten.'),
        ('Fit the channel', 'Insert the channel into the socket and bolt it.'),
    ])

C['channel'] = dict(
    features=[
        ('Modular frames', 'Cut to length and bolt together — no welding needed on site.'),
        ('Slotted face', 'Fix clamps and brackets anywhere along the length.'),
        ('Pairs with our range', 'Works with base plates, cantilevers and leaf clamps.'),
    ],
    install=[
        ('Cut & deburr', 'Cut the channel to length and remove sharp edges.'),
        ('Mount', 'Fix to base plates, cantilevers or directly with anchors.'),
        ('Add fittings', 'Attach clamps and brackets through the slots and tighten.'),
    ])

C['bullet'] = dict(
    features=[
        ('Internally threaded', 'Sits flush with the concrete and accepts threaded rod or a bolt.'),
        ('Ideal overhead', 'The standard choice for hanging rods from concrete ceilings.'),
        ('Removable fixture', 'Remove the rod or bolt later — the anchor stays in place.'),
    ],
    install=[
        ('Drill', 'Drill a straight hole of the diameter and depth recommended for the anchor size.'),
        ('Clean', 'Blow or brush out the dust from the hole.'),
        ('Insert', 'Tap the anchor in until it sits flush with the surface.'),
        ('Set', 'Drive the setting tool with sharp hammer blows until the anchor is fully expanded.'),
    ])

C['pin'] = dict(
    features=[
        ('Quick setting', 'Expands as the pin is driven home — fast, one-step fixing.'),
        ('Through-fixing', 'Install straight through the fixture, no marking-out needed.'),
        ('Firm hold', 'Excellent holding strength in concrete.'),
    ],
    install=[
        ('Drill through', 'Drill through the fixture into the concrete at the anchor diameter.'),
        ('Clean', 'Remove dust from the hole.'),
        ('Insert & drive', 'Insert the anchor and hammer the pin home to expand it.'),
    ])

C['wedge'] = dict(
    features=[
        ('Heavy-duty hold', 'Wedge clip expands as the nut is tightened for a permanent, high-strength fixing.'),
        ('Through-bolt fixing', 'Install straight through the fixture — the hole in the plate is your template.'),
        ('Ready to use', 'Supplied with nut and washer.'),
        ('Two diameters', '10 mm and 12 mm in lengths from 75 mm to 200 mm.'),
        ('Solid concrete', 'Made for structural concrete — slabs, beams, columns and floors.'),
    ],
    install=[
        ('Drill', 'Drill a hole the same diameter as the anchor (10 mm bit for a 10 mm anchor), deeper than the embedment.'),
        ('Clean', 'Blow, brush or vacuum the dust out of the hole.'),
        ('Position the fixture', 'Place the base plate or bracket over the hole.'),
        ('Drive in', 'Tap the anchor through the fixture with the nut on, until the washer meets the fixture.'),
        ('Tighten', 'Tighten the nut to expand the wedge and lock the fixture in place.'),
    ],
    tips=[
        'Use in solid concrete only — not in brick, hollow blocks or plaster.',
        'Choose the length so the anchor passes through the fixture and reaches full embedment.',
        'Pair with base plates (BP) and cantilevers (CL) for channel support systems.',
    ])

C['butterfly'] = dict(
    features=[
        ('Quarter-turn operation', 'Fully open to fully closed with a 90° turn of the lever.'),
        ('Corrosion-resistant disc', 'Stainless steel 304 disc for long life in water service.'),
        ('Strong C.I. body', 'Cast iron body for durability on mains and pump lines.'),
        ('ISI marked', 'Certified quality for projects that require ISI-marked valves.'),
        ('Compact & light', 'Takes far less space and weight than a gate valve of the same size.'),
    ],
    install=[
        ('Align flanges', 'Make sure the pipe flanges are parallel, centred and clean.'),
        ('Open the disc slightly', 'Set the disc a little open so its edge does not touch the flange faces.'),
        ('Insert the valve', 'Place the valve between the flanges and fit all bolts hand-tight.'),
        ('Check the disc', 'Open and close fully to make sure the disc moves freely.'),
        ('Tighten crosswise', 'Tighten the bolts in a diagonal (criss-cross) pattern, evenly all round.'),
    ],
    tips=[
        'Choose Poline or Meet brand as per your project specification.',
        'Avoid extra gaskets or grease unless the valve maker calls for them — follow the valve manual.',
        'Commonly used on fire-fighting, pump-house and water-supply mains.',
    ])

C['ballvalve'] = dict(
    features=[
        ('Service without cutting', 'Double unions let you lift the valve out of the line for repair or replacement.'),
        ('Quarter-turn lever', 'Fast, positive open and shut.'),
        ('Brass ball', 'Smooth, durable sealing surface.'),
        ('Three pipe systems', 'End connectors for PPR, CPVC and UPVC lines.'),
        ('Leak-tight unions', 'O-ring sealed union joints.'),
    ],
    install=[
        ('Take it apart', 'Unscrew both union nuts and remove the end connectors from the valve body.'),
        ('Nut onto pipe', 'Slide each union nut onto the pipe, thread facing the valve.'),
        ('Join the ends', 'PPR: heat-fuse the end connector. CPVC / UPVC: solvent-cement it. Let joints cure.'),
        ('Refit the body', 'Seat the O-rings, place the body between the ends and screw on the union nuts.'),
        ('Tighten & test', 'Hand-tight plus a small turn — do not over-tighten. Test for leaks.'),
    ],
    tips=[
        'Order the version that matches your pipe system: PPR, CPVC or UPVC.',
        'Always remove the valve body before heat-fusing — heat can damage the seats.',
        'Not every size is available in every system — see the item codes below.',
    ])
