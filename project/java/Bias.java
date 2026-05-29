package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A form of AI bias - a deviation that may be perpetuated or
amplified by AI systems. NIST identifies three major categories:
systemic, computational/statistical, and human-cognitive
(Part 1 §3.7; NIST SP 1270).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Bias extends NamedThing {

  private List<String> biasCategory;


}